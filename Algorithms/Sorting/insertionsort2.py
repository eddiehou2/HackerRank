#!/bin/python
def insertionSort(ar):
    for i in xrange(1, len(ar)):
        x = i
        for j in xrange(1, i+1):
            if ar[x] < ar[x-1]:
                temp = ar[x]
                ar[x] = ar[x-1]
                ar[x-1] = temp
                x = x - 1
        print " ".join(map(str, ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
