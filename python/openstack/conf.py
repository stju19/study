#!/bin/env python
#coding:utf-8

from oslo.config import cfg
from podm.common import config

a_opt = cfg.IntOpt('aa',default='100',help='aa')

CONF = cfg.CONF
CONF.register_opt(a_opt)
import pdb;pdb.set_trace()
CONF(default_config_files=['test.conf'])

print CONF.aa