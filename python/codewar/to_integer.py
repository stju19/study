#!/usr/bin/env python
"""
http://www.codewars.com/kata/regexp-basics-parsing-integers
Implement String#to_integer, which should return Integer if object is in one of
formats specified below, or nil otherwise:

    * Optional - or +
    * Base prefix 0b (binary), 0x (hexadecimal), 0o (octal), or in case of no
prefix decimal.
    *Digits depending on base

Any extra characters, including whitespace, make number invalid, in which case
you should return nil.

Digits are case insensitive, but base prefix must be lower case.

"""
"""
from re import compile, match

REGEX = compile(r'[+-]?(0(?P<base>[bxo]))?[\d\w]+\Z')

def to_integer(strng):
    try:
        return int(strng, 0 if match(REGEX, strng).group('base') else 10)
    except (AttributeError, KeyError, ValueError):
        pass
"""
import re


def is_digit(string):
    if string.endswith("\n"):
        return False
    return True if re.match("^[+-]?(0b|0o|0x)?\w+$", string) else False


def to_integer(string):
    scale_map = {"0b": 2, "0o": 8, "0x": 16}
    try:
        scale = scale_map.get(string[1:3] if string[0] in "+-" else string[:2], 10)
        ret = int(string, scale)
        return ret if is_digit(string) else None
    except Exception:
        return None
