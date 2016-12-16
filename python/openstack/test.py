#!usr/bin/python

from routes import Mapper
import pdb

map = Mapper()
#pdb.set_trace()
map.connect('home', '/',controller='main',action='index')
map.resource('test', 'test', controller='test')

val = map.match('/test/12')
print val
