import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
ans = abs(100 - n)

if m != 0:
    b = list(input().split())
else:
    b = []

for i in range(1000001):
    for j in str(i):
        if j in b: 
            break
    else:
        ans = min(ans, len(str(i)) + abs(i - n))
print(ans)