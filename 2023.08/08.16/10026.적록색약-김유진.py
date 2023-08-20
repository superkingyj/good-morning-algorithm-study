import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y, z):   
    if not in_range(x, y): return False
    if visited[x][y]: return False
    if grid[x][y] != z: return False
    return True

def dfs(x, y, z):
    visited[x][y] = True
    
    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]
        if can_go(new_x, new_y, z):
            dfs(new_x, new_y, z)

def chage_grid():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'G': 
                grid[i][j] = 'R'

a = 0
visited = [[False]* N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            a += 1
            dfs(i, j, grid[i][j])

chage_grid()
b = 0
visited = [[False]* N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            b += 1
            dfs(i, j, grid[i][j])

print(a, b)