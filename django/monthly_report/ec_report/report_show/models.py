#!/usr/bin/python
# coding:utf-8
from django.db import models


class EC(models.Model):
    number = models.CharField(u'编号', max_length=40)
    product = models.CharField(u'产品', max_length=50)
    state = models.CharField(u'状态', max_length=40)
    theme = models.CharField(u'主题', max_length=100)
    change_big_type = models.CharField(u'变更大类', max_length=40)
    change_small_type = models.CharField(u'变更小类', max_length=40)
    found_department = models.CharField(u'发现部门', max_length=40)
    submit_date = models.DateTimeField(u'提交日期', auto_now_add=True, editable=True)
    physics_veneer_name = models.CharField(u'物理单板.名称', max_length=40)
    logic_veneer_name = models.CharField(u'逻辑单板.名称', max_length=40)
    voluntary_submit = models.CharField(u'变更活动[变更请求ID].是否主活动', max_length=40)
    team = models.CharField(u'团队', max_length=40)
    repetition = models.CharField(u'重复变更请求编号.编号', max_length=40)
    excel_month = models.CharField(u'表单提交年月', max_length=10)

    def __unicode__(self):
        return self.number
