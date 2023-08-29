import sys

N, M, K = map(int, sys.stdin.readline().split())

dp = [[0] * M for _ in range(N)]

arr = [[0] * M for _ in range(N)]

val = 1
x, y = 0, 0

for i in range(N):
    for j in range(M):
        if val == K:
            x = i
            y = j
        arr[i][j] = val
        val += 1

if K == 0:
    for i in range(N):
        dp[i][0] = 1
    for j in range(M):
        dp[0][j] = 1
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[-1][-1])
                
else:

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    for i in range(x, N):
        for j in range(y, M):
            if i == x and j == y:
                continue
            if i == x or j == y:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
    print(dp[x][y] * dp[-1][-1])
    