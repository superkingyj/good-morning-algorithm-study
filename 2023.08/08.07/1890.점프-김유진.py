import sys

N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

for i in range(N):
    for j in range(N):   
        if i == N-1 and j == N-1: continue
        if grid[i][j] == 0: continue

        if in_range(i, j+grid[i][j]):
            dp[i][j+grid[i][j]] += dp[i][j]
        if in_range(i+grid[i][j], j):
            dp[i+grid[i][j]][j] += dp[i][j]

print(dp[-1][-1])