#!/usr/bin/env python

n = int(input())
marks = {}
for i in range(n):
    name, *m = input().split()
    avg_marks = sum(list(map(float, m))) / 3
    a = {name: avg_marks}
    marks.update(a)
s = input()
print('%.2f' % marks[s])
