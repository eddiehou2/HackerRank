#!/bin/python
# Has timeout issues for very long running tests
def median(a,x):
    numList = []
    x = map(int,x)
    for i in xrange(len(a)):
        if a[i] == "r":
            if len(numList) == 0 or not (x[i] in numList):
                print "Wrong!"
            else:
                numList.remove(x[i])
                printMedian(numList)
        elif a[i] == "a":
            numList = quickSortInsert(numList, x[i])
            printMedian(numList)

def printMedian(numList):
    length = len(numList)
    if length == 0:
        print "Wrong!"
    elif length % 2 == 0:
        result = (numList[length/2 - 1] + numList[length/2])/2.0
        if result == int(result):
            result = int(result)
        print result
    else:
        print (numList[int(length/2)])

def quickSortInsert(numList, value):
    length = len(numList)
    middle = int(length/2)
    if length == 0:
        return [value]
    elif length == 1:
        if numList[0] > value:
            return [value] + numList
        else:
            return numList + [value]
    elif numList[middle] > value:
        return quickSortInsert(numList[:middle], value) + numList[middle:]
    else:
        return numList[:middle] + quickSortInsert(numList[middle:], value)



N = input()
s = []
x = []
for i in range(0, N):
    tmp = raw_input().strip().split(' ')
    s.append(tmp[0])
    x.append(int(tmp[1]))

median(s,x)
