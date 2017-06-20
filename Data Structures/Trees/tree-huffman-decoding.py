"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def decodeHuff(root , s):
    if root == None:
        return

    encodedS = s
    current = root
    for encodedC in encodedS:
        if encodedC == "0":
            current = current.left
        elif encodedC == "1":
            current = current.right

        if current.left == None and current.right == None:
            sys.stdout.write(str(current.data))
            current = root
