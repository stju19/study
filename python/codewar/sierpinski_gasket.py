#!/usr/bin/env python
__author__ = '10183988'


def sierpinski(n):
    for i in range(2**n):
        for j in range(i+1):
            print 'L' if i & j == j else ' ',
        print

sierpinski(3)