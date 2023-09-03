# https://www.acmicpc.net/problem/10164
# 격자 상 경로 라 해서 dxdy 테크닉 문제인줄...
# 격자 내 경우의 수 (dp 문제)
n, m, k = map(int, input().split())

dp = [[0] * m for _ in range(n)]

# 반드시 지나쳐야하는 구간이 없는 경우
if k == 0 :
    for i in range(n) :
        for j in range(m) :
            if i == 0 and j == 0 :
                dp[i][j] = 1
            else :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    print(dp[n-1][m-1])
# 필수경로가 있는 경우
else :
    # 필수 경로의 위치
    x = (k-1) // m
    y = (k-1) % m

    # 필수 경로 이전의 경우의 수
    for i in range(x + 1) :
        for j in range(y + 1) :
            if i == 0 and j == 0 :
                dp[i][j] = 1
            else :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # 필수 경로 이후의 경우의 수
    for i in range(x, n) :
        for j in range(y, m) :
            if x == i and y == j :
                continue
            if x == i :
                dp[i][j] = 1
            elif y == j :
                dp[i][j] = 1
            else :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[x][y] * dp[n-1][m-1])

