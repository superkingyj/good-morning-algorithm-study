import sys
sys.setrecursionlimit(10**6)


T = int(sys.stdin.readline())
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    if not in_range(x,y): return False
    if visited[x][y]: return False
    if grid[x][y] == 0: return False
    return True

def dfs(x, y):
    visited[x][y] = True
    
    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]  
        if can_go(new_x, new_y):
            dfs(new_x, new_y)
    

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    grid = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        grid[x][y] = 1
    
    for i in range(N):
        for j in range(M):
            if can_go(i, j):
                cnt += 1
                dfs(i, j)
                
    print(cnt)