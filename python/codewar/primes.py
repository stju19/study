#!/usr/bin/env python
__author__ = '10183988'


def is_prime(n):
    if n < 2:
        return False
    for i in xrange(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

def prime(num):
        primer = []
        plist = [0, 0] + range(2, 7001)
        for i in xrange(2, 7001):
            if plist[i]:
                plist[i+i::i] = [0] * len(plist[i+i::i])
        primer = filter(None, plist)
        return primer[:num]

class Primes:
    primes = []

    @classmethod
    def first(cls, n):
        cls.primes = []
        var = 3
        cls.primes.append(2)
        while len(cls.primes) < n:
            if is_prime(var):
                cls.primes.append(var)
            var += 2
        return cls.primes[:n]



