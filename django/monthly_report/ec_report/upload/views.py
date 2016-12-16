# -*- coding:utf-8 -*-
import os
import django
from django.shortcuts import render
from report_show.models import EC
import logging
import xlrd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "upload.settings")
django.setup()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(os.getcwd() + '/log/', 'upload_views_log.txt'),
                    filemode='w')
log = logging.getLogger('root')
# Create your views here.


def upload(request):
    if request.method == 'POST':
        try:
            upload_result = handle_upload_file(request.FILES.get('upload_excel'))
        except AttributeError:
            log.warning(u"没有选择上传文件")
            upload_result = u'请先选择文件，然后点击上传'
        return render(request, 'upload.html', {'upload_result': upload_result})
    return render(request, 'upload.html')


def handle_upload_file(upload_file):
    file_name = "history_files/" + upload_file.name
    upload_result = ""
    if os.path.exists(file_name):
        upload_result = u'文件已覆盖同名文件，'
    destination = open(file_name, 'wb')
    for chunk in upload_file.chunks():
        destination.write(chunk)
    destination.close()
    log.debug(upload_result + u'上传成功，文件路径为：' + file_name)
    load_excel(file_name)
    return upload_result + u'上传成功'


def load_excel(file_name):

    sheet_name = "Sheet1"
    month = os.path.splitext(file_name)[0][-6:]
    try:
        data = xlrd.open_workbook(file_name)
        log.debug(u'打开本地excel文件成功')
        table = data.sheet_by_name(sheet_name)
        log.debug(u'打开本地excel工作表%s成功', sheet_name)
        row_number = table.nrows

        name_map = {}
        for j, k in enumerate(table.row_values(0)):
            name_map.update({k: j})

        ec_list = [EC(
            number=table.row_values(i)[name_map[u'编号']],
            product=table.row_values(i)[name_map[u'产品']],
            state=table.row_values(i)[name_map[u'状态']],
            theme=table.row_values(i)[name_map[u'主题']],
            change_big_type=table.row_values(i)[name_map[u'变更大类']],
            change_small_type=table.row_values(i)[name_map[u'变更小类']],
            found_department=table.row_values(i)[name_map[u'发现人部门']],
            submit_date=table.row_values(i)[name_map[u'提交日期']],
            physics_veneer_name=table.row_values(i)[name_map[u'物理单板名.名称']],
            logic_veneer_name=table.row_values(i)[name_map[u'逻辑单板名.名称']],
            voluntary_submit=table.row_values(i)[name_map[u'变更活动[变更请求ID].是否主活动']],
            team=table.row_values(i)[name_map[u'团队']],
            repetition=table.row_values(i)[name_map[u'重复变更请求编号.编号']],
            excel_month=month) for i in range(1, row_number)]
        EC.objects.bulk_create(ec_list)
    except:
        log.debug(u'打开本地excel工作表%s失败', file_name)
        log.exception('exception')
