#!/bin/python
def insertionSort(ar):
    temp = ar[len(ar) - 1]
    i = len(ar) - 1
    while i-1 >= 0 and temp < ar[i-1]:
        ar[i] = ar[i-1]
        i -= 1
        print " ".join(map(str,ar))
    ar[i] = temp
    print " ".join(map(str,ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
