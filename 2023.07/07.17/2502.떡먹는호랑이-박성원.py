import sys

d, k = map(int, sys.stdin.readline().split())

dp = [0]*(d+1)
dp[0] = 0
dp[1] = 1

while True :
    for i in range(2, len(dp)) :
        dp[i] = dp[i-1] + dp[i-2]

    if dp[-1] == k :
        ans = dp[-1]
        break

    if dp[-1] < k :
        dp[1] += 1

print(dp)