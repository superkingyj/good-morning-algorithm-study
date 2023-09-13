n, k = map(int, input().split())
dp = [[1]*(k+1) for _ in range(n+1)]

for i in range(1, k+1):
    for j in range(i+1, n+1):
        dp[j][i] = dp[j-1][i-1] + dp[j-1][i]

print(dp[n][k]%10007)