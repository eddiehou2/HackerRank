#!/bin/python

import sys


S = raw_input().strip()
count = 0
i = 0
while i < len(S) - 2:
    if S[i] != 'S':
        count += 1
    if S[i+1] != 'O':
        count += 1
    if S[i+2] != 'S':
        count += 1
    i += 3
print count
