#!/usr/bin/env python


class A(object):
    def __init__(self):
        self.a = 1

    @property
    def test(self):
        pass

    @test.getter
    def test(self):
        return self.a

    @test.setter
    def test(self, value):
        self.a = value


a = A()
a.test = 3
print a.test