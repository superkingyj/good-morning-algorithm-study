import sys

N, M, K = map(int, sys.stdin.readline().split())
DP = [[0] * M for _ in range(N)]
result = 1 

if K == 0:
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0:
                DP[i][j] = 1
                continue
            DP[i][j] = DP[i][j-1]+DP[i-1][j]
   
    result = DP[-1][-1] 
else:
    target_x = (K-1) // M
    target_y = (K-1) % M
    
    for i in range(target_x+1):
        for j in range(target_y+1):
            if i == 0 or j == 0:
                DP[i][j] = 1
                continue
            DP[i][j] = DP[i][j-1]+DP[i-1][j]
    
    result *= DP[target_x][target_y]
    
    for i in range(target_x, N):
        for j in range(target_y, M):
            if i == target_x or j == target_y:
                DP[i][j] = 1
                continue
            DP[i][j] = DP[i][j-1]+DP[i-1][j]
    
    result *= DP[-1][-1]

print(result)