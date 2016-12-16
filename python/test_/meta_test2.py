#!/usr/bin/env python
from types import FunctionType


def deco(func):
    def _deco(*args, **kwargs):
        print 'deco'
        return func(*args, **kwargs)
    return _deco


class deco_meta(type):
    def __new__(cls, name, bases, dct):
        import pdb;pdb.set_trace()
        for name, value in dct.iteritems():
            if name not in ('__metaclass__', '__init__', '__module__') and\
                type(value) == FunctionType:
                value = deco(value)

            dct[name] = value

        return type.__new__(cls, name, bases, dct)


class meta_test(object):
    __metaclass__ = deco_meta
    def __init__(self):
        print self.a

    def a(self):
        print 'a'

    def b(self):
        print 'b'


print meta_test().a()
