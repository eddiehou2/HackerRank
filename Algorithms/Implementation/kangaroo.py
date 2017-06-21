#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    dif = abs(x1 - x2)
    increasing = False
    while not increasing:
        if x1 == x2:
            return "YES"
        else:
            x1 = x1 + v1
            x2 = x2 + v2
            if dif <= abs(x1 - x2):
                increasing = True
                return "NO"
            else:
                dif = abs(x1-x2)

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
