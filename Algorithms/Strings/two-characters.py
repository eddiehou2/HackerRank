#!/bin/python

import sys


s_len = int(raw_input().strip())
s = raw_input().strip()

letterArr = []
for i in xrange(len(s)):
    if not (s[i] in letterArr):
        letterArr.append(s[i])

maxLength = 0
alt = True
for i in xrange(len(letterArr)-1):
    for j in xrange(i+1, len(letterArr)):
        lastCharacter = ""
        length = 0
        alt = True
        for c in xrange(len(s)):
            if s[c] == letterArr[i] or s[c] == letterArr[j]:
                if lastCharacter == s[c]:
                    alt = False
                    break
                else:
                    lastCharacter = s[c]
                    length += 1
        if alt:
            maxLength = max(maxLength, length)

print maxLength
        
