import sys
input = sys.stdin.readline

X = int(input())
club_line = input().strip()
stack = []
for p in club_line:
    stack.append(p)

stack = list(reversed(stack))
w = 0
m = 0

while stack:
    cur = stack.pop()
    if cur == 'W':
        if abs((w+1) - m) <= X:
            w += 1
        elif stack and abs((w+1) - m) > X:
            next = stack.pop()
            if next == 'M':
                if abs((m+1) - w) <= X:
                    m += 1
                    stack.append(cur)
            else:
                break
        else:
            break
    else:
        if abs((m+1) - w) <= X:
            m += 1
        elif stack and abs((m+1) - w) > X:
            next = stack.pop()
            if next == 'W':
                if ((w+1) - m) <= X:
                    w += 1
                    stack.append(cur)
            else:
                break
        else:
            break
print(w + m)