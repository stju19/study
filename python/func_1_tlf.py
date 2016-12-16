#!/usr/bin/env python
__author__ = '10183988'
#!/usr/bin/env python

A = [
    [{'a': 1}],
    [{'a': 2}, {'a': 2}],
    [{'a': 3}, {'a': 4}, {'a': 5}]
]


B = [
    [{'a': 1}],
    [{'a': 2}, {'a': 3}],
    [{'a': 3}, {'a': 4}, {'a': 5}]
]

temp = [list(set([d['a'] for d in item])) for item in B]
print temp
sum = []
for item in temp:
    sum.extend(item)
print sum
if len(sum) != len(set(sum)):
    raise TypeError()
