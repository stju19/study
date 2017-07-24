#!/usr/bin/env python
# coding:utf-8
"""
1.接受一个字符串，去掉其中的所有空格。
2.给出一个整形值，返回该值对应的月份英文单词。比如输入10返回“October”。
3.用户输入三个数字：f(from)、t(to)、i(increment)。以i为步长，从f数到t，包括f和t。例如，如果输入的是f==2、t==26、i==4，程序将输出2，6，10，14，18，22，26。
4.定义一个Person类，包含setName和getName两种方法。
5.颠倒字典中的键和值。用一个字典做输入，输出另一个字典，用前者的键做值，前者的值做键。
"""
from datetime import datetime


def trim_space(string):
    return string.replace(" ", "")


def get_month_fullname(num):
    return datetime(2000, num, 1).strftime("%B")


def slice_print(f, t, i):
    for value in range(f, t, i):
        print value,
    print


class Persion(object):
    _name = None
    def setName(self, value):
        self._name = value

    def getName(self):
        return self._name


class NewPersion(object):
    _name = None
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


def reverse_dict(input):
    return dict(zip(input.values(), input.keys()))

print "No. 1"
print trim_space("a bcd  e ")

print "No. 2"
print get_month_fullname(4)

print "No. 3"
slice_print(2, 26, 4)

print "No. 4"
person=NewPersion()
person.name = '123'
print "persion.name: %s" % person.name

print "No. 5"
print reverse_dict({"a":1, "b": 2, "z": 26})

