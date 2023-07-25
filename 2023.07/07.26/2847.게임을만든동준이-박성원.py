import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]

ans = 0

for i in range(n-1, 0, -1) :
    if li[i] <= li[i-1] :
        ans += (li[i-1] - li[i] + 1)
        li[i-1] = li[i] - 1

print(ans)
