import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

q = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

Notvisited = False
result = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            Notvisited = True
        
        result = max(result, arr[i][j])
    
    
if Notvisited:
    print(-1)
else:
    print(result - 1)    
        