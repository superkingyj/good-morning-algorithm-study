import sys
from pprint import pprint
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
grid = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
dz, dx, dy = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1] # 위, 아래, 앞, 뒤, 왼, 오
target = []
result = 0

def init_target():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if grid[i][j][k] == 1: 
                    target.append((i, j, k))

def in_range(x, y, z):
    return 0 <= x < N and 0 <= y < M and 0 <= z < H

def can_go(x, y, z):
    if not in_range(x, y, z): return False
    if visited[z][x][y]: return False
    if grid[z][x][y] == -1: return False
    return True

def bfs():
    global result
    q = deque()
    
    for z, x, y in target:
        visited[z][x][y] = True 
        q.append((z, x, y, 0))
    
    while q:
        z, x, y, cnt = q.popleft()
        result = max(result, cnt)
        
        for i in range(6):
            new_z, new_x, new_y = z+dz[i], x+dx[i], y+dy[i]
            
            if can_go(new_x, new_y, new_z):
                visited[new_z][new_x][new_y] = True
                q.append((new_z, new_x, new_y, cnt+1))

def check():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                # 방문하지 않았고 익지 않은 토마토이면
                if not visited[i][j][k] and grid[i][j][k] == 0: return False
    return True


init_target()
bfs()
if check(): print(result)
else: print(-1)