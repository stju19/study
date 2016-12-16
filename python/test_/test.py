#!/usr/bin/env python
import pdb
# class PositiveInteger(int):
#
#   def __new__(cls, value):
#
#     return super(PositiveInteger, cls).__new__(cls, abs(value))
#
# i = PositiveInteger(-3)
# print i

class A(object):
    a=1
    def __init__(self):
        self.b=1

    def fun(self):
        A.a+=1

A().fun()
A().fun()
print A.a