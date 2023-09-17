N, M = map(int, input().split())

dp = [[0] * (M+1) for _ in range(N+1)]

dp[1][1] = 1


for i in range(1, N+1):
    for k in range(1, M+1):
        if i == 1 and k == 1:
            continue
        dp[i][k] = (dp[i-1][k] + dp[i][k-1] + dp[i-1][k-1]) % 1000000007

print(dp[N][M])