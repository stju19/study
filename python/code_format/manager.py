# Copyright (c) 2010 OpenStack Foundation
# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Scheduler Service
"""
from datetime import datetime
import thread
import time

from oslo.config import cfg
from oslo import messaging
from podm import context
from podm import manager
from podm.openstack.common import importutils
from podm.openstack.common import log as logging
from podm.openstack.common.threadpool import ThreadPool
from podm.openstack.common import periodic_task
from podm.states import *
from podm.concrete import inspect_tmc
from podm.concrete.aging_data import AgingData
from podm.concrete.driver.data_convert import ConvertDBData


concrete_thread_num_opts = [
    cfg.IntOpt('concrete_collect_res_thread_num',
               default=10,
               help='create thread pool to collect resource'),
    cfg.IntOpt('concrete_collect_state_thread_num',
               default=10,
               help='create thread pool to collect server state')]

concrete_interval_opts = [
    cfg.IntOpt('concrete_update_resource_interval',
               default=60,
               help='interval to collect resource'),
    cfg.IntOpt('concrete_update_state_interval',
               default=10,
               help='interval to collect server state'),
    cfg.IntOpt('concrete_inspect_tmc_interval',
               default=300,
               help='interval to inspect tmc and ip')]

concrete_driver_opt = cfg.StrOpt('concrete_driver',
                                 default='podm.concrete.driver.tmc_driver.TmcDriver',
                                 help='concrete driver to perform server-related operations')

CONF = cfg.CONF
CONF.register_opts(concrete_thread_num_opts)
CONF.register_opts(concrete_interval_opts)
CONF.register_opt(concrete_driver_opt)

LOG = logging.getLogger(__name__)


class ConcreteManager(manager.Manager):
    """Send cmd to TMC to create server.Collect all resources state"""

    RPC_API_VERSION = '1.0'

    target = messaging.Target(version=RPC_API_VERSION)

    def __init__(self, service_name=None, *args, **kwargs):
        super(ConcreteManager, self).__init__(*args, **kwargs)
        self.inspector = inspect_tmc.InspectManager("abc")
        self.data_handle = ConvertDBData()
        self.aging_data = AgingData()
        self.driver = importutils.import_object(CONF.concrete_driver)
        self.ResCollectThPool = ThreadPool(CONF.concrete_collect_res_thread_num)
        self.StateCollectThPool = ThreadPool(
            CONF.concrete_collect_state_thread_num)

    def resources_collect(self, context):
        rc_start_time = datetime(1, 1, 1)
        while True:
            rc_period = datetime.utcnow() - rc_start_time
            rc_start_time = datetime.utcnow().replace(microsecond=0)

            host_urls = self.inspector.get_host_urls(context)
            for host_url in host_urls:
                self.ResCollectThPool.queueTask(self.driver.service_root,
                                                (host_url, '/rest/v1/'))
            self.ResCollectThPool.waitFinish(interval=1)

            self.aging_data.aging_resource(rc_start_time)
            self.aging_data.aging_tmc(rc_period)

            time.sleep(CONF.concrete_update_resource_interval)

    def need_update_server_state(self, last_action, task_state, server_state):
        if server_state == SERVER_DELETED or \
                        task_state == TASK_SCHEDULING:
            return False
        else:
            return True

    @periodic_task.periodic_task(spacing=CONF.concrete_inspect_tmc_interval,
                                 run_immediately=True)
    def inspect_tmc(self, context):
        self.inspector.inspect_tmc()


    def servers_state_collect(self, context):
        while True:
            servers = self.db.servers_get_all(context)
            # high_prior_servers=[]
            # low_prior_servers=[]
            # for server in servers:
            #     if not server.deleted:
            #         continue
            #
            #     server=dict(server)
            #     if self.need_update_server_state(server['deleted_at'],
            #                      server['task_state'], server['node_state']):
            #         if server['task_state'] == TASK_STABLE:
            #             low_prior_servers.append(server)
            #         else:
            #             # TASK_SPAWNING,TASK_STOPPING,TASK_DELETING...
            #             # new request command, get these server state first
            #             high_prior_servers.append(server)
            #
            # query_servers = high_prior_servers+low_prior_servers
            for server in servers:
                self.StateCollectThPool.queueTask(
                    self.driver.server_state_collect, (context, server))

            self.StateCollectThPool.waitFinish(interval=1)

            time.sleep(CONF.concrete_update_state_interval)

    def init_host(self):
        ctxt = context.get_admin_context()
        thread.start_new_thread(self.resources_collect, (ctxt,))
        thread.start_new_thread(self.servers_state_collect, (ctxt,))
        # second arg need be a tuple.  (ctxt,) is tuple, (ctxt) is not tuple

    def create_server(self, context, server_properties, weighed_resource):
        self.driver.create_server(context, server_properties, weighed_resource)

    def delete_server(self, context, system_id):
        return self.driver.delete_server(context, system_id)

    def reset_blade(self, context, lid, type):
        return self.driver.reset_blade(context, lid, {'ResetType': type})

    def config_blade(self, context, lid, config):
        return self.driver.config_blade(context, lid, config)

    def config_port(self, context, lid, config):
        return self.driver.config_port(context, lid, config)

    def reset_machine(self, context, system_id, body):
        return self.driver.reset_machine(context, system_id, body)
