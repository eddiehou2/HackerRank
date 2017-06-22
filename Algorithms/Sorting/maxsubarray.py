# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

T = input()
for test in xrange(T):
    N = input()
    array = map(int, sys.stdin.readline().split(' '))
    cArr = []
    ncArr = []
    smallestNeg = -sys.maxsize-1
    for i in xrange(N):
        if i == 0:
            if array[i] < 0:
                cArr.append(0)
                ncArr.append(0)
                smallestNeg = max(smallestNeg, array[i])
            else:
                cArr.append(array[i])
                ncArr.append(array[i])
        else:
            if array[i] < 0:
                ncArr.append(ncArr[i-1])
                cArr.append(max(array[i] + cArr[i-1], 0))
                smallestNeg = max(smallestNeg, array[i])
            else:
                cArr.append(max(array[i] + cArr[i-1], array[i]))
                ncArr.append(ncArr[i-1] + array[i])

    cMaxSum = max(cArr)
    ncMaxSum = ncArr[len(ncArr) - 1]
    print str(cMaxSum if cMaxSum > 0 else smallestNeg) + " " + str(ncMaxSum if ncMaxSum > 0 else smallestNeg)
