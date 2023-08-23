import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    maxval = 0
    minval = 10001
    for j in range(i, 0, -1):
        maxval = max(maxval, arr[j - 1])
        minval = min(minval, arr[j - 1])
        dp[i] = max(dp[i], dp[j - 1] + maxval - minval)

print(dp[N])