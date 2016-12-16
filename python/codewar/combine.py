#!/usr/bin/env python
__author__ = '10183988'


def combine(a, *args):
    ret = a.copy()
    for obj in args:
        for i in obj:
            if i in ret:
                ret[i] += obj[i]
            else:
                ret[i] = obj[i]
    return ret


objA = {'a': 10, 'b': 20, 'c': 30}
objB = {'a': 3, 'c': 6, 'd': 3}
objC = {'a': 5, 'd': 11, 'e': 8}
objD = {'c': 3}