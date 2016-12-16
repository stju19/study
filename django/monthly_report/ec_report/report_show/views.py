# coding:utf-8
from django.shortcuts import render,render_to_response
from django.db.models import Q
from report_show.models import EC
import os
import logging
import json
from .forms import MonthForm
from django.http import HttpResponse

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(os.getcwd() + '/log/', 'report_show_views_log.txt'),
                    filemode='w')
log = logging.getLogger('root')


show_dict = {'wait_confirm_refuse': u'待确认拒绝',
             'wait_review': u'待审核',
             'implementing': u'实施中',
             'confirmed_refuse': u'已确认拒绝',
             'wait_research': u'待研究',
             'closed': u'已关闭',
             'reported': u'已上报',
             'wait_relate_handle': u'待关联请求处理',
             'wait_confirm_repeat': u'待确认重复',
             'invalid': u'已作废',}
time = '201508'
month = '08'

def index(request):
    form = select_month(request)

    log.debug('index.html request content: %s', request.__dict__)

    summary = {}
    obj_filter = EC.objects.filter
    summary['month'] = month
    summary['total_number'] = EC.objects.filter(excel_month=time).count()
    summary['requirement_number'] = obj_filter(change_big_type=u'需求').filter(excel_month=time).count()
    summary['optimization_number'] = obj_filter(change_big_type=u'优化').filter(excel_month=time).count()
    summary['refused_or_canceled_number'] = obj_filter(Q(state=u'已确认拒绝') | Q(state=u'已作废')).filter(excel_month=time).count()
    summary['repetition_number'] = obj_filter(~Q(repetition=u'')).filter(excel_month=time).count()
    summary['self_commit_number'] = obj_filter(found_department=u'平台软件一部/中心研究院/战略及平台').filter(excel_month=time).count()
    if summary['total_number'] > 0:
        summary['leak_rate'] = float("%.2f" % (100 * (1.0 - summary['self_commit_number'] /
                                                      float(summary['total_number']))))
    else:
        summary['leak_rate'] = 0
    summary['internal_leak_number'] = obj_filter(found_department__contains=u'/中心研究院/战略及平台').filter(excel_month=time).count() - \
                                         summary['self_commit_number']
    summary['carry_out_number'] = obj_filter(state=u'实施中').filter(excel_month=time).count()
    summary['total_valid_number'] = obj_filter(~Q(state=u'已确认拒绝')).filter(excel_month=time).count()

    log.debug('index.html summary : ')
    for key in summary:
        log.debug('%s : %s', key, summary[key])

    return render(request, 'index.html', {
        'summary': summary,
        'form': form
    })


def state(request):
    form = select_month(request)
    log.debug('state.html request content: %s', request.__dict__)

    state_dict = {}
    state_dict['month'] = month
    all_objects_nums = EC.objects.filter(excel_month=time).count()
    for key, value in show_dict.items():
        state_dict[key+'_nums'] = EC.objects.filter(state=value).filter(excel_month=time).count()
        state_dict[key] = EC.objects.filter(state=value)
        if all_objects_nums > 0:
            state_dict[key+'_percent'] = float("%.2f" % (100 * state_dict[key+'_nums'] / float(all_objects_nums)))
        else:
            state_dict[key+'_percent'] = 0
    state_dict['all_objects_nums'] = all_objects_nums

    log.debug('state.html state_dict : ')
    for key in state_dict:
        log.debug('%s : %s', key, state_dict[key])
        if hasattr(state_dict[key], '__iter__') :
            for item in state_dict[key]:
                log.debug('%s', item)

    sector_graph = get_sector_graph(show_dict, state_dict)
    return render(request, 'state.html', {
        'state_dict': state_dict,
        'sector_graph': sector_graph,
        'form': form
    })


def style(request):
    form = select_month(request)

    style_name_mapping = {u'a_deadly': u'A-致命', u'b_serious': u'B-严重', u'c_general': u'C-一般', u'd_slight': u'D-轻微',
                          u'add': u'新增', u'change': u'修改', u'delete': u'删除', u'optimize': u'优化'}
    style_dict = {}
    style_dict['month'] = month
    obj_filter = EC.objects.filter
    style_dict[u'all_objects_nums'] = EC.objects.filter(excel_month=time).count()
    for key in style_name_mapping:
        style_dict[key] = obj_filter(change_small_type=style_name_mapping[key])
        style_dict[key + u'_count'] = obj_filter(change_small_type=style_name_mapping[key]).filter(excel_month=time).count()
        if style_dict[u'all_objects_nums'] > 0:
            style_dict[key + u'_percent'] = float('%.2f' % (100 * style_dict[key + u'_count'] /
                                                            float(style_dict[u'all_objects_nums'])))
        else:
            style_dict[key + u'_percent'] = 0

    sector_graph = get_sector_graph(style_name_mapping, style_dict)
    return render(request, 'style.html', {
        'style_dict': style_dict,
        'sector_graph': sector_graph,
        'form': form
        })


def team(request):
    form = select_month(request)

    team_list = [u'CG', u'CT、MIDWARE', u'DAISY', u'HCN', u'NAIL', u'TULIP']
    state_dict = []
    for team_name in team_list:
        team_state_dict = {}
        team_summation = EC.objects.filter(team=team_name).filter(excel_month=time).count()
        ec_list_team = EC.objects.filter(team=team_name).filter(excel_month=time)
        team_state_dict['team_name'] = team_name
        team_state_dict['team_summation'] = team_summation
        for key, value in show_dict.items():
            team_state_dict[key+'_count'] = ec_list_team.filter(state=value).filter(excel_month=time).count()
            team_state_dict[key] = ec_list_team.filter(state=value).filter(excel_month=time).filter(excel_month=time)
            if team_summation > 0:
                team_state_dict[key+'_percent'] = 100 * team_state_dict[key+'_count'] / team_summation
            else:
                team_state_dict[key+'_percent'] = 0
        state_dict.append(team_state_dict)
    return render(request, 'team.html', {
        'state_dict': state_dict,
        'month': month,
        'form': form
    })


def get_sector_graph(show_dict, statistics_dict):
    backup_color = ['Pink', 'Gray', 'DeepSkyBlue', 'Orange',
                    'Purple', 'HotPink', 'Coral', 'White',
                    'Cyan', 'Green', 'Olive', 'Yellow',
                    'Blue', 'Lime', 'Red', 'Black']

    (graph_text, graph_data, graph_color) = ([], [], [])
    for key, value in show_dict.items():
        graph_text.append(value)
        if statistics_dict['all_objects_nums'] > 0:
            graph_data.append(statistics_dict[key+'_percent']/100)
        graph_color.append(backup_color.pop())

    sector_graph = {
        'graph_data': json.dumps(graph_data),
        'graph_color': json.dumps(graph_color),
        'graph_text': json.dumps(graph_text)
    }
    return sector_graph


def select_month(request):
    global time, month
    if request.method == 'POST':
        form = MonthForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            time = '2015' + str(month)
    else:
        form = MonthForm()

    return form