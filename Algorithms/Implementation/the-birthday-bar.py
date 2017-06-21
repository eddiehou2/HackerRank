#!/bin/python

import sys

def solve(n, s, d, m):
    ways = 0
    chocolateArray = []
    cur_sum = 0
    finished = False
    i = 0
    while not finished:
        if i >= len(s):
            finished = True
        elif cur_sum + s[i] <= d:
            cur_sum += s[i]
            chocolateArray.append(s[i])
            if cur_sum == d and len(chocolateArray) == m:
                    ways += 1
            i += 1
        else:
            if len(chocolateArray) > 0:
                removed = chocolateArray.pop(0)
                cur_sum -= removed
            else:
                finished = True

    return ways

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
