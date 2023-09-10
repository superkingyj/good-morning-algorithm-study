import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def init():
    ripe_tomatos = []
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                ripe_tomatos.append((i, j))
    
    return ripe_tomatos

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x,y):
    if not in_range(x,y): return False
    if visited[x][y]: return False
    if grid[x][y] == -1: return False
    else: return True
    
def bfs(ripe_tomatos):
    q = deque()
    total_time = 0
    
    for x, y in ripe_tomatos:
        visited[x][y] = True
        q.append((x, y, 0))
    
    while q:
        x, y, cnt = q.popleft()
        total_time = max(total_time, cnt)
        
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y, cnt+1))
    
    return total_time

ripe_tomatos = init()
answer = bfs(ripe_tomatos)

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 and not visited[i][j]:
            answer = -1
            
print(answer)
