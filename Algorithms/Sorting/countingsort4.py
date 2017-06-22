# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

countArr = []
for i in xrange(100):
    countArr.append([])
n = input()
for i in xrange(n):
    line = sys.stdin.readline().strip().split(" ")
    word = line[1]
    index = int(line[0])
    if i < n//2:
        word = "-"
    countArr[index].append(word)

sentence = []
for i in xrange(100):
    for j in xrange(len(countArr[i])):
        sentence.append(countArr[i][j])

print " ".join(sentence)
