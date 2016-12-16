#!/usr/bin/env python
__author__ = '10183988'


f = open("word_lib.txt")
l = []
for i in f.readlines():
    l.append(i.split(' ')[0])

ret = filter(lambda x: len(x) == 9, l)

fout = open('ret.txt', 'w')
fout.writelines([i + ' 'for i in ret])


