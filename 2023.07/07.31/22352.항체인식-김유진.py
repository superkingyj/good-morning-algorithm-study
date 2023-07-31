import sys
from pprint import pprint

N, M = map(int, sys.stdin.readline().split())
before = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
after = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
flag = True
cnt = 0

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y, from_):
    if not in_range(x,y): return False
    if visited[x][y]: return False
    if before[x][y] != from_: return False
    return True

def dfs(x, y, from_, to_):
    visited[x][y] = True
    before[x][y] = to_
    
    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]
        if can_go(new_x, new_y, from_):
            dfs(new_x, new_y, from_, to_)

def check():
    for i in range(N):
        for j in range(M):
            if before[i][j] != after[i][j]: return False
    return True

for i in range(N):
    for j in range(M):
        
        # 백신으로 변경된 곳이 아니면서 before와 after가 다르다면 
        if not visited[i][j] and before[i][j] != after[i][j]:
            cnt += 1
            dfs(i, j, before[i][j], after[i][j])
        
        # 백신으로 변경된 곳인데 before와 after가 다르다면
        elif visited[i][j] and before[i][j] != after[i][j]:
            flag = False
            break
    if not flag: break

if not flag or cnt >= 2: print("NO")
else:
    if check(): print("YES")
    else: print("NO")