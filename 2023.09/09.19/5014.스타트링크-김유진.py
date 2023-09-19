import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [False] * (F+1)
q = deque()
cnt = 0

def in_range(v):
    return 0 < v <= F

def bfs():
    global cnt
    visited[S] = True
    q.append((S,0))

    while q:
        v, c = q.popleft()

        if v == G:
            cnt = c
            break
        
        for i in range(2):
            if i == 0: new_v = v+U
            else: new_v = v-D
            if in_range(new_v) and not visited[new_v]:
                visited[new_v] = True
                q.append((new_v, c+1))

bfs()
if visited[G]: print(cnt)
else: print("use the stairs")