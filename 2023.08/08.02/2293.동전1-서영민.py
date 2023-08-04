import sys

n, k = map(int, input().split())

coin = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0 for _ in range(k+1)]

dp[0] = 1

for i in coin:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])