#!/bin/python

import sys

def solve(grades):
    for i in xrange(len(grades)):
        if grades[i] >= 38:
            finalGrade = ((grades[i] + 2)/5)*5
            grades[i] = finalGrade if finalGrade > grades[i] else grades[i]
    return grades

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
