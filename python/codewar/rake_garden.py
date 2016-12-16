#!/usr/bin/env python
__author__ = '10183988'

def rake_garden(garden):
    return ' '.join(map(lambda x: x if x == 'rock' else 'gravel', garden.split(' ')))

print rake_garden('slug spider rock gravel gravel gravel gravel gravel gravel gravel')