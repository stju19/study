#!/usr/bin/env python

from datetime import datetime, tzinfo, timedelta

ZERO = timedelta(0)


class Utc(tzinfo):
    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


class Mytz(tzinfo):
    def __init__(self, hours, name=''):
        super(Mytz, self).__init__()
        self.__offset = timedelta(hours=hours)
        self.__name = name

    def __eq__(self, other):
        if isinstance(other, Mytz):
            return (
                (other.__offset == self.__offset)
                and
                (other.__name == self.__name)
            )
        if isinstance(other, tzinfo):
            return other == self
        return False

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return ZERO

    def __repr__(self):
        return "<Mytz %r %r>" % (self.__name, self.__offset)

