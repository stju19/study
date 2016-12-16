#! /usr/bin/python
# -*- coding: utf-8 -*-
import re
import httplib


class _HTTPClient(object):
    def __init__(self):
        self.client = None

    def connect(self, host, **kwargs):
        self.client = httplib.HTTPConnection(host, timeout=5, **kwargs)

    def get(self, url):
        self.client.request('GET', url)
        response = self.client.getresponse()
        reason = response.reason
        status = response.status
        body = response.read()
        return status, body


class PodmLib(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        self.pod = 1
        self.client = _HTTPClient()
        self.map = self._init_map()

    def _init_map(self):
        return {
            'Racks': 'racks', 'Drawers': 'drawers',
            'ComputeModules': 'computemodules', 'Blades': 'blades',
            'Processors': 'processors', 'Memory': 'memory',
            'StorageControllers': 'storagecontrollers', 'Drives': 'drives',
            'FabricModules': 'fabricmodules', 'Switches': 'switches',
            'Ports': 'ports', 'Managers': 'managers',
            'PowerZones': 'powerzones', 'Psus': 'psus',
            'ThermalZones': 'thermalzones', 'Fans': 'fans'
        }

    def get_body_from_tmc(self, host, path):
        """
        根据所给的tmc的url，发起GET请求，返回接收的body体

        example:
        | ${body}= | Get Body From Tmc | 10.43.211.133:8082 | /rest/v1/ |

        - body是一个字典
        """
        self.client.connect(host)
        status, body = self.client.get(path)
        return eval(body)

    def get_links_from_body(self, body):
        """
        给定podm的list接口中的body，返回list接口中所有的'Links'中的url

        example:
        ${body}=
        {
            "Name":"Compute Module Collection",
            "Modified":"",
            "Links":{
                "Members@odata.count":1,
                "Members":[{
                        "@odata.id":"/rest/v1/Pods/1/Racks/7/Drawers/14/ComputeModules/1"
                    },
                    {
                        "@odata.id":"/rest/v1/Pods/1/Racks/7/Drawers/14/ComputeModules/2"
                    }]
            }
        }
        | ${ids} | Get Links From Body | ${body} |
        =>
        ${ids} = ["/rest/v1/Pods/1/Racks/7/Drawers/14/ComputeModules/1","/rest/v1/Pods/1/Racks/7/Drawers/14/ComputeModules/1"]
        """
        urls = []
        for path_dict in body.get('Links', {}).get('Members', []):
            urls.append(path_dict.get('@odata.id', ''))
        return urls

    def cli_to_dict(self, cli_str):
        """
        将podmclient的命令行输出表格转化成字典

        cli_str =\n
        +-------------+------------------------------------------------------------------+\n
        | Property    | Value                                                            |\n
        +-------------+------------------------------------------------------------------+\n
        | @odata.id   | /rest/v1/Pods/1/Racks/7                                          |\n
        | ChassisType | Rack                                                             |\n
        | EnumStatus  | None                                                             |\n
        | Id          | 7                                                                |\n
        | Links       | {u'Drawers': {u'@odata.id': u'/rest/v1/Pods/1/Racks/7/Drawers'}, |\n
        |             | u'Oem': {}, u'ManagedBy': [{u'@odata.id':                        |\n
        |             | u'/rest/v1/Pods/1/Racks/7/Managers/1'}]}                         |\n
        +-------------+------------------------------------------------------------------+

        example:
        | ${body}= | Cli To Dict | ${cli_str} |
        =>

        ${body}=\n
        {'@odata.id': '/rest/v1/Pods/1/Racks/7',
         'ChassisType': 'Rack',
         'EnumStatus': 'None',
         'Id': '7',
         'Links':{'Drawers':{u'@odata.id': u'/rest/v1/Pods/1/Racks/7/Drawers'},
                  u'Oem': {},
                  u'ManagedBy': [{u'@odata.id':'/rest/v1/Pods/1/Racks/7/Managers/1'}]
                 }
        }

        """
        lines = cli_str.splitlines()[3:-1]
        temp = ''
        for line in lines:
            line_list = re.split(' *\| *', line)[1:3]
            if line_list[0]:
                temp += ',"' + line_list[0] + '":"' + line_list[1] + '"'
            else:
                temp = temp[:-1] + line_list[1] + '"'
        temp = '{' + temp[1:] + '}'
        temp = re.sub('"{', '{', temp)
        temp = re.sub('}"', '}', temp)
        return eval(temp)

    def get_id_list_by_type(self, ip_list, lid_type):
        """
        根据给定的tmc的ip:port和关键字，返回所有的与该关键字相关的id集合信息

        参数：
        - ip_list：一个列表或列表的字符串；
        - lid_type 参见podm接口文档，可选项为：Racks, Drawers, ComputeModules, Blades,
        Processors, Memory, StorageControllers, Drives, FabricModules, Switches,
        Ports, Managers, PowerZones, Psus, ThermalZones, Fans.

        example:
        | ${id_list} | Get Id List By Type | ['10.43.211.62:8080','10.43.211.133:8082'] | ComputeModules |
        =>

        ${id_list}=\n
        [{'ip': '10.43.211.62:8080', 'pod': 1, 'rack': 1, 'module': 1, 'drawer': 1},\n
         {'ip': '10.43.211.62:8080', 'pod': 1, 'rack': 1, 'module': 2, 'drawer': 1},\n
         {'ip': '10.43.211.62:8080', 'pod': 1, 'rack': 1, 'module': 3, 'drawer': 1},\n
         {'ip': '10.43.211.133:8082', 'pod': 1, 'rack': 7, 'module': 2, 'drawer': 14}\n
        ]
        """
        lid_type = self.map.get(lid_type, '') or lid_type
        if isinstance(ip_list, basestring):
            ip_list = eval(ip_list)
        if lid_type in ('racks', 'drawers'):
            lid_type = 'racks_and_drawers'
        method = self.__getattribute__('_get_%s' % lid_type)
        ids_list = method(ip_list, [])

        return ids_list

    def _get_id_from_body(self, body):
        ids = []
        for path_dict in body.get('Links', {}).get('Members', []):
            ids.append(int(path_dict.get('@odata.id', '').split('/')[-1]))

        return ids

    def _get_racks_and_drawers(self, ip_list, ids_list):
        for ip in ip_list:
            body = self.get_body_from_tmc(ip, '/rest/v1/')
            rack_id = int(body['Id'].split('.')[0])
            drawer_id = int(body['Id'].split('.')[1])
            ids_list.append({'ip': ip, 'pod': self.pod, 'rack': rack_id,
                             'drawer': drawer_id})
        return ids_list

    def _get_computemodules(self, ip_list, ids_list):
        ids_list = self._get_racks_and_drawers(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/ComputeModules" % id_list['drawer']
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            ids = self._get_id_from_body(body)
            for id in ids:
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'module': id})
        return ids_list

    def _get_blades(self, ip_list, ids_list):
        ids_list = self._get_computemodules(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/ComputeModules/%s/Blades"\
                       % (id_list['drawer'], id_list['module'])
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            ids = self._get_id_from_body(body)
            for id in ids:
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'module': id_list['module'],
                                 'blade': id})
        return ids_list

    def _get_processors(self, ip_list, ids_list):
        ids_list = self._get_blades(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/ComputeModules/%s/Blades/%s/Processors"\
                       % (id_list['drawer'], id_list['module'], id_list['blade'])
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            ids = self._get_id_from_body(body)
            for id in ids:
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'module': id_list['module'],
                                 'blade': id_list['blade'],
                                 'processor': id})
        return ids_list

    def _get_memory(self, ip_list, ids_list):
        ids_list = self._get_blades(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/ComputeModules/%s/Blades/%s/Memory"\
                       % (id_list['drawer'], id_list['module'], id_list['blade'])
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            ids = self._get_id_from_body(body)
            for id in ids:
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'module': id_list['module'],
                                 'blade': id_list['blade'],
                                 'memory': id})
        return ids_list

    def _get_storagecontrollers(self, ip_list, ids_list):
        ids_list = self._get_blades(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            (rack_id, drawer_id, module_id, blade_id) = \
                (id_list['rack'], id_list['drawer'], id_list['module'], id_list['blade'])
            url_path = "/rest/v1/Drawers/%s/ComputeModules/%s/Blades/%s/StorageControllers"\
                       % (id_list['drawer'], id_list['module'], id_list['blade'])
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            ids = self._get_id_from_body(body)
            for id in ids:
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'module': id_list['module'],
                                 'blade': id_list['blade'],
                                 'storage': id})
        return ids_list

    def _get_drives(self, ip_list, ids_list):
        ids_list = self._get_storagecontrollers(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/ComputeModules/%s/Blades/%s/StorageControllers/%s/Drives"\
                       % (id_list['drawer'], id_list['module'], id_list['blade'], id_list['storage'])
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            ids = self._get_id_from_body(body)
            for id in ids:
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'module': id_list['module'],
                                 'blade': id_list['blade'],
                                 'storage': id_list['storage'],
                                 'drive': id})
        return ids_list

    def _get_fabricmodules(self, ip_list, ids_list):
        ids_list = self._get_racks_and_drawers(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/FabricModules" % id_list['drawer']
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            ids = self._get_id_from_body(body)
            for id in ids:
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'module': id})
        return ids_list

    def _get_switches(self, ip_list, ids_list):
        ids_list = self._get_fabricmodules(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/FabricModules/%s/Switches"\
                       % (id_list['drawer'], id_list['module'])
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            ids = self._get_id_from_body(body)
            for id in ids:
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'module': id_list['module'],
                                 'switch': id})
        return ids_list

    def _get_ports(self, ip_list, ids_list):
        ids_list = self._get_switches(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/FabricModules/%s/Switches/%s/Ports"\
                       % (id_list['drawer'], id_list['module'], id_list['switch'])
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            ids = self._get_id_from_body(body)
            for id in ids:
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'module': id_list['module'],
                                 'switch': id_list['switch'],
                                 'port': id})
        return ids_list

    def _get_managers(self, ip_list, ids_list):
        ids_list = self._get_racks_and_drawers(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Managers"
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            ids = self._get_id_from_body(body)
            for id in ids:
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'manager': id})
        return ids_list

    def _get_networkservice(self, ip_list, ids_list):
        pass

    def _get_ethernetinterfaces(self, ip_list, ids_list):
        pass

    def _get_powerzones(self, ip_list, ids_list):
        ids_list = self._get_racks_and_drawers(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/PowerZones" % id_list['drawer']
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            for pz in body['PowerZones']:
                pz_id = int(pz['Links']['@odata.id'].split('/')[-1])
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'powerzone': pz_id})
        return ids_list

    def _get_psus(self, ip_list, ids_list):
        ids_list = self._get_powerzones(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/PowerZones/%s/Psus"\
                       % (id_list['drawer'], id_list['powerzone'])
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            for psu in body['Psus']:
                psu_id = int(psu['Links']['@odata.id'].split('/')[-1])
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'powerzone': id_list['powerzone'],
                                 'psu':psu_id})
        return ids_list

    def _get_thermalzones(self, ip_list, ids_list):
        ids_list = self._get_racks_and_drawers(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/ThermalZones" % id_list['drawer']
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            for tz in body['ThermalZones']:
                tz_id = int(tz['Links']['@odata.id'].split('/')[-1])
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'thermalzone': tz_id})
        return ids_list

    def _get_fans(self, ip_list, ids_list):
        ids_list = self._get_thermalzones(ip_list, ids_list)
        temp_ids_list, ids_list = ids_list, []
        for id_list in temp_ids_list:
            url_path = "/rest/v1/Drawers/%s/ThermalZones/%s/Fans"\
                       % (id_list['drawer'], id_list['thermalzone'])
            body = self.get_body_from_tmc(id_list['ip'], url_path)
            for fan in body['Fans']:
                fan_id = int(fan['Links']['@odata.id'].split('/')[-1])
                ids_list.append({'ip': id_list['ip'], 'pod': self.pod,
                                 'rack': id_list['rack'],
                                 'drawer': id_list['drawer'],
                                 'thermalzone': id_list['thermalzone'],
                                 'fan':fan_id})
        return ids_list

podm = PodmLib()
# import pdb;pdb.set_trace()
# '10.43.166.18:8082'
print podm.get_id_list_by_type(['10.43.211.133:8082'], 'ComputeModules')
# print podm.get_id_list_by_type(['10.43.211.62:8080'], 'blades')