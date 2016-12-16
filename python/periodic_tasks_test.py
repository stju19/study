#!/usr/bin/env python

from podm import manager
from podm.openstack.common import periodic_task
from podm.openstack.common import loopingcall
import time

class TestManager(manager.Manager):
        def __init__(self, *args, **kwargs):
            self.count = 0
            super(TestManager, self).__init__(*args, **kwargs)

        @periodic_task.periodic_task(spacing=5, run_immediately=False)
        def foooooo(self, context=None):
            self.count += 1
            print time.ctime(), "One-Two, buckle my shoe"

        @periodic_task.periodic_task(spacing=10, run_immediately=False)
        def baaaaar(self, context=None):
            self.count += 1
            print time.ctime(), "Three-Four, open the door"

        @periodic_task.periodic_task(spacing=15, run_immediately=False)
        def panda(self, context=None):
            print time.ctime(),"Five-Six, pick up sticks"


test_manager = TestManager('abc')
periodic = loopingcall.LoopingCall(test_manager.periodic_tasks, context=None)
periodic.start(interval=0.8753, initial_delay=0)
periodic.wait()
