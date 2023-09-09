import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [[0]*M for _ in range(N)]
cnt = min(N, M) // 2

for i in range(cnt):
    dq = deque()
    dq.extend(grid[i][i:M-i])
    dq.extend([row[M-i-1] for row in grid[i+1:N-i-1]])
    dq.extend(grid[N-i-1][i:M-i][::-1])
    dq.extend([row[i] for row in grid[i+1:N-i-1]][::-1])
    
    dq.rotate(-R)
    
    for j in range(i, M-i):
        result[i][j] = dq.popleft()
    for j in range(i+1, N-i-1):
        result[j][M-i-1] = dq.popleft()
    for j in range(M-i-1, i-1, -1):
        result[N-i-1][j] = dq.popleft()  
    for j in range(N-i-2, i, -1):
        result[j][i] = dq.popleft()    

for line in result:
    print(*line)