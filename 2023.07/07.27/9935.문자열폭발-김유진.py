import sys

string = sys.stdin.readline().rstrip()
bomb = list(sys.stdin.readline().rstrip())
l = len(bomb)
stack = []

for ch in string:
    stack.append(ch)
    if stack[-l:] == bomb:
        stack[-l:] = []

if stack: print("".join(stack))
else: print("FRULA")