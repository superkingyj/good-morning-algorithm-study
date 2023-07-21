import sys
from collections import deque

N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
q = deque()
height = 0
max_height = 0
max_safe_area = 0
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def get_max_height():
    global max_height
    for i in range(N):
        max_height = max(max_height, max(grid[i]))

def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

def can_go(x,y):
    if not in_range(x,y): return False
    elif visited[x][y]: return False
    elif grid[x][y] <= height: return False
    else: return True

def bfs(x,y):
    visited[x][y] = True
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

get_max_height()

for h in range(0, max_height+1):
    height = h
    safe_area = 0
    for i in range(N):
        for j in range(N):
            if can_go(i,j):
                safe_area += 1
                bfs(i,j)

    max_safe_area = max(max_safe_area, safe_area)
    visited = [[False] * N for _ in range(N)]

print(max_safe_area)