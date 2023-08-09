import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1


for i in range(N):
    for j in range(N):
        temp = arr[i][j]
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break
        
        if j + temp < N:
            dp[i][j + temp] += dp[i][j]
        
        if i + temp < N:
            dp[i + temp][j] += dp[i][j]