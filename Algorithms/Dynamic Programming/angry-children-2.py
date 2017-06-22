# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Timing complexity is too slow

def unfairness(diffArray):
    unfairness = 0
    length = len(diffArray)
    for i in xrange(length):
        unfairness += diffArray[i] * (length-i) * (i+1)
    return unfairness

n = int(raw_input())
k = int(raw_input())
candies = []
for i in xrange(0, n):
    candies.append(int(raw_input()))

differences = [0]
candies.sort()
for i in xrange(1,n):
    differences.append(candies[i] - candies[i-1])


min_unfairness = sys.maxsize
for i in xrange(k, n):
    unfairness_score = unfairness(differences[i-(k-1):i])
    min_unfairness = min(unfairness_score, min_unfairness)

print min_unfairness
