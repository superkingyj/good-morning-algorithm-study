import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

cave = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
idx = 0


def check_air(i, j):
    visited = [[False] * C for _ in range(R)]
    q = deque()
    visited[i][j] = True
    q.append((i, j))
    while q:
        x, y = q.popleft()
        if x == R - 1:
            return False
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and cave[nx][ny] == 'x':
                q.append((nx, ny))
                visited[nx][ny] = True
    return True

def fall_cluster(i, j):
    bottom = {}
    all_block = []
    visited = [[False] * C for _ in range(R)]
    q = deque()
    visited[i][j] = True
    q.append((i, j))      
    while q:
        x, y = q.popleft()
        bottom[y] = max(bottom.get(y, 0), x)
        all_block.append((x, y))
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and cave[nx][ny] == 'x':
                q.append((nx, ny))
                visited[nx][ny] = True
    for o, p in bottom.items():
        for np in range(p + 1, R):
            if cave[np][o] == 'x':
                bottom[o] = np - 1 - p
                break
        else:
            bottom[o] = R - 1 - p
            
    fall = min(bottom.values())
    
    for x, y in all_block:
        cave[x][y] = '.'
        
    for x, y in all_block:
        cave[x + fall][y] = 'x'

for i in arr:
    T = 0
    if idx % 2 == 0:
        for j in range(len(cave[R - i])):
            if cave[R - i][j] == 'x':
                cave[R - i][j] = '.'
                for k in range(4):
                    nx, ny = R - i + dx[k], j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and cave[nx][ny] == 'x':
                        if check_air(nx, ny):
                            fall_cluster(nx, ny)
                break
    else:
        for j in range(len(cave[R - i]) - 1, -1, -1):
            if cave[R - i][j] == 'x':
                cave[R - i][j] = '.'
                for k in range(4):
                    nx, ny = R - i + dx[k], j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and cave[nx][ny] == 'x':
                        if check_air(nx, ny):
                            fall_cluster(nx, ny)
                break
    idx += 1
    
    
for i in range(R):
    for j in range(C):
        print(cave[i][j], end='')     
    print()
