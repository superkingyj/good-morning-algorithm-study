import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = [sys.stdin.readline() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
q = deque()

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    if not in_range(x,y): return False
    elif visited[x][y]: return False
    elif grid[x][y] == "0": return False
    else: return True

def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    visited[0][0] = 1
    q.append((0,0,1))

    while q:
        x,y,z = q.popleft()
        for i in range(4):
            new_x, new_y = x+dxs[i], y+dys[i]
            if can_go(new_x, new_y):
                visited[new_x][new_y] = z+1
                q.append((new_x, new_y, z+1))

bfs()
print(visited[-1][-1])