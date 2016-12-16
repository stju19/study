#!/usr/bin/env python
__author__ = '10183988'

import re
from podmclient import utils

cli_str = \
"""+-------------------+-----------------------------------------------------------------------------------------------------+
| Property          | Value                                                                                               |
+-------------------+-----------------------------------------------------------------------------------------------------+
| @odata.context    | /rest/v1/$metadata#RSAPods/Links/Members/1/Links/Racks/Links/Members/$entity                        |
| @odata.id         | /rest/v1/Pods/1/Racks/7                                                                             |
| @odata.type       | #RSARack.1.0.0.RSARack                                                                              |
| ChassisType       | Rack                                                                                                |
| EnumStatus        | None                                                                                                |
| Id                | 7                                                                                                   |
| Links             | {u'Drawers': {u'@odata.id': u'/rest/v1/Pods/1/Racks/7/Drawers'}, u'Oem': {}, u'ManagedBy':          |
|                   | [{u'@odata.id': u'/rest/v1/Pods/1/Racks/7/Managers/1'}]}                                            |
| Location          | {u'Pod': 1, u'Rack': 7}                                                                             |
| Modified          |                                                                                                     |
| Name              | None                                                                                                |
| RSARackAttributes | {u'RackUUID': None, u'AssertTag': None, u'FRUInfo': {u'SerialNumber': None, u'Manufacturer': None}, |
|                   | u'GeoTag': None, u'RMMPresent': False, u'TrayPresent': {u'Trays': [{u'TrayRuid': 14}],              |
|                   | u'TraysNumber': 1}, u'RackSupportsDisaggregatedPowerCooling': False}                                |
| Status            | {u'HealthRollup': None, u'State': u'Enabled', u'Health': u'OK'}                                     |
+-------------------+-----------------------------------------------------------------------------------------------------+
"""

def cli_to_dict(string):
    lines = string.splitlines()[3:-1]
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

# lines = cli_str.splitlines()[3:-1]
# temp = ''
# for line in lines:
#     line_list = re.split(' *\| *', line)[1:3]
#     print line_list
# import pdb;pdb.set_trace()
s = cli_to_dict(cli_str)
print s


