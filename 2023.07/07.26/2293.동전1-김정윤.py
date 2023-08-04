import sys

N, K = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for i in range(N)]

dp = [0] * (K + 1)

# 동전이 하나만 쓰일 때
dp[0] = 1

for i in arr:
    for j in range(i, K + 1):
        dp[j] += dp[j - i]

print(dp[K])