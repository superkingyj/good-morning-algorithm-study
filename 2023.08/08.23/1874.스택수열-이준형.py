from sys import stdin

input = stdin.readline
n = int(input())

sb = []
stack = []
start = 0
for _ in range(n):
    val = int(input())
    if val > start:
        for i in range(start + 1, val + 1):
            stack.append(i)
            sb.append('+')
        start = val
    elif stack[-1] != val:
        print("NO")
        exit()
    stack.pop()
    sb.append('-')

print(*sb,sep='\n')

