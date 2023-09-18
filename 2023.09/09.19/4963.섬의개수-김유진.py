import sys
from collections import deque

dx, dy = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]

def in_range(x,y):
    return 0 <= x < N and 0 <= y < M

def can_go(x,y):
    if not in_range(x,y): return False
    if visited[x][y]: return False
    if grid[x][y] == 0: return False
    return True

def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append((x,y))
    
    while q:
        x, y = q.popleft()
        for i in range(8):
            new_x, new_y = x + dx[i], y + dy[i]
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))
    

while True:
    M, N = map(int, sys.stdin.readline().split())
    
    if N == 0 and M == 0:
        break
    
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and grid[i][j] == 1:
                cnt += 1
                bfs(i, j)
                
    print(cnt)