#!/usr/bin/env python

def circle (path):
    x = y = 0
    for i in range(len(path)):
        direction = path[i]
        if direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        elif direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
    return x, y

s = input()
a = circle(s)

if a == (0, 0):
    print('True')
else:
    print('False')
