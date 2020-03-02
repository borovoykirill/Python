#!/usr/bin/env python

l0 = input()
keys = l0.split(' ')
l1 = input()
result = {}
values = l1.split(' ')
l2 = len(keys) - len(values)
for i in range(len(values)):
    result.update({keys[i]: values[i]})
if len(keys) > len(values):
    for i in range(l2):
        result.update({keys[len(values) + i]: "None"})
print(result)
