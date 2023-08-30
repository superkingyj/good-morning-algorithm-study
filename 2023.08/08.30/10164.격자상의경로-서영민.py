N, M, K = map(int, input().split())


if K > 0:
    x, y = (K-1) // M , (K-1) % M
else:
    x, y = 0, 0

dp = [[0]*(y+1) for _ in range(x+1)]
dp[0][0] = 1
for i in range(x+1):
    for k in range(y+1):
        if i - 1 >= 0 and k - 1 >= 0:
            dp[i][k] = dp[i-1][k] + dp[i][k-1]
        elif i - 1 >= 0 and k - 1 < 0:
            dp[i][k] = dp[i-1][k]
        elif i - 1 < 0 and k - 1 >= 0:
            dp[i][k] = dp[i][k-1]

res1 = dp[x][y]
dp = [[0]*(M-y) for _ in range(N-x)]
dp[0][0] = 1
for i in range(N-x):
    for k in range(M-y):
        if i - 1 >= 0 and k - 1 >= 0:
            dp[i][k] = dp[i-1][k] + dp[i][k-1]
        elif i - 1 >= 0 and k - 1 < 0:
            dp[i][k] = dp[i-1][k]
        elif i - 1 < 0 and k - 1 >= 0:
            dp[i][k] = dp[i][k-1] 

res2 = dp[-1][-1]
print(res1*res2)   