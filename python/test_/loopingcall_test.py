#!/usr/bin/env python
__author__ = '10183988'

from podm.openstack.common import loopingcall


def hello_world():
    print 'hello world'


loop = loopingcall.LoopingCall(hello_world)
loop.start(interval=0.1, initial_delay=0)
loop.wait()