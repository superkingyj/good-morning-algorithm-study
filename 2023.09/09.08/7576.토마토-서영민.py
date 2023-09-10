from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

def bfs(init_list):
    q = deque()
    for codi in init_list:
        q.append(codi)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        
        for a, b in zip(dx, dy):
            nx = x + a
            ny = y + b
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))

init = []
for i in range(N):
    for k in range(M):
        if box[i][k] == 1:
            init.append((i, k))

bfs(init) 

res = -1
flag = False
for i in range(N):
    if flag:
        break
    for k in range(M):
        if box[i][k] == 0:
            res = -1
            flag = True
            break
        res = max(res, box[i][k])
if res != -1:
    print(res - 1)
else:
    print(res)