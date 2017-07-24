#!/usr/bin/env python
__author__ = '10183988'

def add_1(func):
    def _deco(a):
        print a
        return func() + 1
    return _deco

@add_1(1)
def func1():
    return 1

@add_1
def func2():
    return 2

import pdb;pdb.set_trace()
print func1()
print func2()

