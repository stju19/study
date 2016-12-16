# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=40, verbose_name='\u7f16\u53f7')),
                ('product', models.CharField(max_length=50, verbose_name='\u4ea7\u54c1')),
                ('state', models.CharField(max_length=40, verbose_name='\u72b6\u6001')),
                ('theme', models.CharField(max_length=100, verbose_name='\u4e3b\u9898')),
                ('change_big_type', models.CharField(max_length=40, verbose_name='\u53d8\u66f4\u5927\u7c7b')),
                ('change_small_type', models.CharField(max_length=40, verbose_name='\u53d8\u66f4\u5c0f\u7c7b')),
                ('found_department', models.CharField(max_length=40, verbose_name='\u53d1\u73b0\u90e8\u95e8')),
                ('submit_date', models.DateTimeField(auto_now_add=True, verbose_name='\u63d0\u4ea4\u65e5\u671f')),
                ('physics_veneer_name', models.CharField(max_length=40, verbose_name='\u7269\u7406\u5355\u677f.\u540d\u79f0')),
                ('logic_veneer_name', models.CharField(max_length=40, verbose_name='\u903b\u8f91\u5355\u677f.\u540d\u79f0')),
                ('voluntary_submit', models.CharField(max_length=40, verbose_name='\u53d8\u66f4\u6d3b\u52a8[\u53d8\u66f4\u8bf7\u6c42ID].\u662f\u5426\u4e3b\u6d3b\u52a8')),
                ('team', models.CharField(max_length=40, verbose_name='\u56e2\u961f')),
                ('repetition', models.CharField(max_length=40, verbose_name='\u91cd\u590d\u53d8\u66f4\u8bf7\u6c42\u7f16\u53f7.\u7f16\u53f7')),
                ('excel_month', models.CharField(max_length=10, verbose_name='\u8868\u5355\u63d0\u4ea4\u5e74\u6708')),
            ],
        ),
    ]
