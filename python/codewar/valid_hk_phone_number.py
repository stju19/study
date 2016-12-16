#!/usr/bin/env python
__author__ = '10183988'
import re


def is_valid_HK_phone_number(number):
    return re.match('^\d{4} \d{4}$', number) is not None


def has_valid_HK_phone_number(number):
    return re.match('.*\d{4} \d{4}.*', number) is not None


assert is_valid_HK_phone_number('1234 5678') is True
assert is_valid_HK_phone_number('5893 5483') is True
assert is_valid_HK_phone_number('15893 5483') is False
assert is_valid_HK_phone_number('589 35483') is False

assert has_valid_HK_phone_number('sklfjsdklfjsf') is False
assert has_valid_HK_phone_number('     1234 5678   ') is True
assert has_valid_HK_phone_number('s4293042904820482409209438dslfdjs9345 8234sdklfjsdkfjskl28394723987jsfss2') is True