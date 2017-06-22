#!/bin/python
def partition(ar):
    p = ar[0]
    left = []
    equal = []
    right = []
    for i in xrange(len(ar)):
        if ar[i] == p:
            equal.append(ar[i])
        elif ar[i] > p:
            right.append(ar[i])
        elif ar[i] < p:
            left.append(ar[i])

    print " ".join(map(str, left)) + " " + " ".join(map(str, equal)) + " " + " ".join(map(str, right))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
