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
    code="a"
    def __init__(self):
        self.str = self.code

    def fun(self):
        import pdb;pdb.set_trace()
        error_msg = "a PDUAlarm subclass must implement get_valid_addinfo"
        raise NotImplementedError(error_msg)

class B(A):
    code="b"
    # def fun(self):
    #     print "B" + self.str

class C(A):
    code="c"
    def fun(self):
        print "C" + self.str

bb=B()
bb.fun()

cc=C()
cc.fun()