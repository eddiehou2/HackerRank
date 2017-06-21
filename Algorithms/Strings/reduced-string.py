#!/bin/python

import sys

def super_reduced_string(s):
    found = True
    while found:
        i = 0
        found = False
        while i < len(s)-1 and not found:
            if s[i] == s[i+1]:
                if i < len(s) - 2:
                    s = s[:i] + s[i+2:]
                else:
                    s = s[:i]
                found = True
            i += 1

    if len(s) == 0:
        return "Empty String"
    else:
        return s

s = raw_input().strip()
result = super_reduced_string(s)
print(result)
