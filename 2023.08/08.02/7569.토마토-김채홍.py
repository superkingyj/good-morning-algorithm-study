import sys
from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

m, n, h = map(int, input().split())

matrix = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

visited = [[[False]*m for _ in range(n)] for _ in range(h)]

queue = deque()

answer = 0

def bfs():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if matrix[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                queue.append((nx,ny,nz))
                matrix[nx][ny][nz] = matrix[x][y][z] + 1
                visited[nx][ny][nz] = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1 and visited[i][j][k] == 0:
                queue.append((i,j,k))
                visited[i][j][k] = True
bfs()

for i in matrix:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)            
        answer = max(answer, max(j))

print(answer-1)
