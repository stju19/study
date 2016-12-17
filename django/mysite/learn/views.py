# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    value = {
        "string": 'hello',
        "list": [1, 2, 3, 4],
        "dict": {'a': 11, 'b': 22}
    }
    return render(request, 'home.html', value)


def add(request, a, b):
    return HttpResponse(1)
