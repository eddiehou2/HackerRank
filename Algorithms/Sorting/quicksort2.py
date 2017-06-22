#!/bin/python
def quick_sort(ar):
    if len(ar) < 2:
        return ar

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
    left = quick_sort(left)
    right = quick_sort(right)
    together = left + equal + right
    print " ".join(map(str, together))
    return together


m = input()
ar = [int(i) for i in raw_input().strip().split()]
quick_sort(ar)
