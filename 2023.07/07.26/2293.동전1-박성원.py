import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1

for i in li :
    for j in range(i, k+1) :
        if j-1 >= 0:
            dp[j] += dp[j-i]

print(dp[k])