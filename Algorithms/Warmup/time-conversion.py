#!/bin/python

import sys

def timeConversion(s):
    if s[len(s)-2] == "P" and int(s[0:2]) != 12:
        newHour = str(int(s[0:2]) + 12)
        return newHour + s[2:-2]
    elif s[len(s)-2] == "A" and int(s[0:2]) == 12:
        return "00" + s[2:-2]
    return s[:-2]

s = raw_input().strip()
result = timeConversion(s)
print(result)
