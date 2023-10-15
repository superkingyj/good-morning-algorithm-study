import sys

N, M = map(int, sys.stdin.readline().split())
arr = []

for i in range(N):
    arr.append((list(map(int, sys.stdin.readline().split()))))

dp = [[0] * (M + 1) for _ in range(N + 1)]
    
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]    

K = int(sys.stdin.readline())

for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])