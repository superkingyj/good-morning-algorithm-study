import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

DP = [sys.maxsize] * (N+1)
DP[0] = 0

for i in range(N+1):
    for k in range(i+1):
        DP[i] = min(DP[i], DP[i-k] + arr[k])

print(DP[-1])
