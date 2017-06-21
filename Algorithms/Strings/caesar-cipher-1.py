#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
k = k % 26
newString = []
for i in xrange(len(s)):
    if s[i].isalpha():
        upper = s[i].isupper()
        newChar = ord(s[i]) + k
        while not chr(newChar).isalpha() or chr(newChar).isupper() != upper:
            newChar -= (ord('Z') - ord('A') + 1)
        newString.append(chr(newChar))
    else:
        newString.append(s[i])

print "".join(newString)
