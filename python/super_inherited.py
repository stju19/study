#!/usr/bin/env python
import pdb

class A(object):
    def __init__(self):
        """ A """
        print 'A start'
        # pdb.set_trace()
        super(A, self).__init__()
        print 'A end'


class B(A):
    def __init__(self):
        """ B """
        print 'B start'
        # pdb.set_trace()
        super(B, self).__init__()
        print 'B end'


class C(A):
    def __init__(self):
        """ C """
        print 'C start'
        # pdb.set_trace()
        super(C, self).__init__()
        print 'C end'


class D(A):
    def __init__(self):
        """ D """
        print 'D start'
        super(D, self).__init__()
        print 'D end'

class E(C, D):
    def __init__(self):
        """ E """
        print 'E start'
        super(E, self).__init__()
        print 'E end'

class F(B, E):
    def __init__(self):
        """ F """
        print 'F start'
        super(F, self).__init__()
        print 'F end'

print F.__mro__
print E.__mro__
# print B.__mro__
# print C.__mro__
# D()
F()
