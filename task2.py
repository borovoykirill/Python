#!/usr/bin/env python

keys = input().split()
l0 = len(keys)
result = {}
values = input().split()
l1 = len(values)
for i in range(min(l0, l1)):
    result.update({keys[i]: values[i]})
l2 = abs(l0 - l1)
if l0 > l1:
    for i in range(l2):
        result.update({int(keys[l1 + i]): None})
s = str(result)
print(s.replace("'", ''))
