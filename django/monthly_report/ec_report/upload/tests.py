# coding:utf-8
from django.test import TestCase
from django.test import Client
from report_show.models import EC
import xlwt
import xlrd
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(os.getcwd() + '/log/', 'upload_tests_log.txt'),
                    filemode='w')
log = logging.getLogger('root')
# Create your tests here.


class TestUpload(TestCase):

    def setUp(self):
        self.url = '/upload/'
        self.send_file_name = 'send_file.xls'
        self.receive_file_path = r'history_files\send_file.xls'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        self.test_data = [
            (0, 0, u'编号'),
            (1, 0, u'614004808394'),
            (0, 1, u'产品'),
            (1, 1, u'ZXOPENCOS'),
            (0, 2, u'状态'),
            (1, 2, u'待确认拒绝'),
            (0, 3, u'主题'),
            (1, 3, u'【vGW】实例化完成，但后续虚机相关操作异常（跟P1.B3需要多租户相关）'),
            (0, 4, u'变更大类'),
            (1, 4, u'缺陷/故障'),
            (0, 5, u'变更小类'),
            (1, 5, u'C-一般'),
            (0, 6, u'发现人部门'),
            (1, 6, u'UNC测试二部/无线研究院/无线产品经营部'),
            (0, 7, u'发现活动'),
            (1, 7, u'系统测试'),
            (0, 8, u'当前处理人'),
            (1, 8, u''),
            (0, 9, u'研究负责人'),
            (1, 9, u''),
            (0, 10, u'提交日期'),
            (1, 10, u'2015-08-31 18:47:14'),
            (0, 11, u'发现子系统.名称'),
            (1, 11, u'ceilometer'),
            (0, 12, u'物理单板名.名称'),
            (1, 12, u''),
            (0, 13, u'逻辑单板名.名称'),
            (1, 13, u''),
            (0, 14, u'变更活动[变更请求ID].是否主活动'),
            (1, 14, u''),
            (0, 15, u'变更活动[变更请求ID].定位代码配置项.配置项名称'),
            (1, 15, u''),
            (0, 16, u'变更活动[变更请求ID].变更活动负责人.用户名称'),
            (1, 16, u''),
            (0, 17, u'变更活动[变更请求ID].定位代码配置项.所属科室'),
            (1, 17, u''),
            (0, 18, u'重复变更请求编号.编号'),
            (1, 18, u''),
            (0, 19, u'指派实施时间'),
            (1, 19, u''),
            (0, 20, u'变更活动[变更请求ID].变更配置项类型'),
            (1, 20, u''),
            (0, 21, u'变更活动[变更请求ID].状态.状态名称'),
            (1, 21, u''),
            (0, 22, u'团队'),
            (1, 22, u'HCN'),
        ]
        for item in self.test_data:
            ws.write(item[0], item[1], item[2])
        wb.save(self.send_file_name)
        log.info(u"创建excel文件成功")
        try:
            test_data_obj = EClist.objects.get(number=u'614004808394')
            if test_data_obj is not None:
                test_data_obj.delete()
                log.info("""setUp test "number=u'614004808394'" database exist, and already deleted""")
        except:
            log.info("""setUp test "number=u'614004808394'" database not exist, so do not need to delete""")

        self.client = Client()

    def tearDown(self):

        try:
            test_data_obj = EC.objects.get(number=u'614004808394')
            if test_data_obj is not None:
                test_data_obj.delete()
                log.info("""tearDown test "number=u'614004808394'" database exist, and already deleted""")
        except:
            log.info("""tearDown test "number=u'614004808394'" database not exist, so do not need to delete""")

        if os.path.exists(self.send_file_name):
            os.remove(self.send_file_name)
        if os.path.exists(self.receive_file_path):
            os.remove(self.receive_file_path)

        del self.client

    def test_upload(self):
        """
        first open send_file to transfer file,the pointer will at the end of the file after transfer,
        so need to open twice this file twice.
        """
        with open(self.send_file_name, 'rb') as obj_send_file:
            response = self.client.post(self.url, data={'upload_excel': obj_send_file})
            obj_send_file.close()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists(self.receive_file_path))

        wb = xlrd.open_workbook(self.send_file_name)
        ws = wb.sheet_by_name("Sheet1")
        row_number = ws.nrows
        col_number = ws.ncols
        self.assertEqual(row_number, 2)
        self.assertEqual(col_number, 23)
        for item in self.test_data:
            self.assertEqual(ws.cell(item[0], item[1]).value, item[2])
