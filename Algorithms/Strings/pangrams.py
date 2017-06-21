# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

s = sys.stdin.readline()
alpha = []
for i in xrange(26):
    alpha.append(0)

s = s.lower()
for i in xrange(len(s)):
    if s[i].isalpha():
        alpha[ord(s[i]) - ord('a')] = 1

if min(alpha) == 0:
    print "not pangram"
else:
    print "pangram"
