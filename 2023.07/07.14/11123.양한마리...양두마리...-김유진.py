import sys
from collections import deque
T = int(sys.stdin.readline())
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1] 

def in_range(x, y):
    return 0 <= x < H and 0 <= y < W

def can_go(x, y):
    if not in_range(x,y): return False
    if visited[x][y]: return False
    if grid[x][y] != "#": return False
    return True
    
def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append((x,y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

for _ in range(T):
    H, W = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    cnt = 0
    
    for i in range(H):
        for j in range(W):
            if can_go(i, j):
                cnt += 1
                # print(i, j, cnt)
                bfs(i, j)
    
    print(cnt)