# coding:utf-8
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .form import AddForm


def index(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据
        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})


def home(request):
    value = {
        "string": 'hello1',
        "list": [1, 2, 3, 4],
        "dict": {'a': 11, 'b': 22}
    }
    return render(request, 'home.html', value)


def add(request, a, b):
    add_sum = int(a) + int(b)
    return HttpResponse(str(add_sum))
