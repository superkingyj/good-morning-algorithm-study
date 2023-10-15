import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for k in range(1, M+1):
        dp[i][k] = dp[i-1][k] + dp[i][k-1] + arr[i-1][k-1] - dp[i-1][k-1]
    

for _ in range(K):
    i, j, x, y = map(int,input().split())
    print(dp[x][y] - (dp[i-1][y] + dp[x][j-1]) + dp[i-1][j-1])