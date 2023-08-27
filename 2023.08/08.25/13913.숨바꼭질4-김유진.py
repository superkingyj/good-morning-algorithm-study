import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [False] * 100001
path = [-1] * 100001

def in_range(x):
    return 0 <= x <= 100000

def get_path(x):
    result = [x]
    while path[x] != -1:
        result = [path[x]] + result
        x = path[x]
    return result

def bfs():
    q = deque()
    visited[N] = True
    q.append((N, 0))

    while q:
        x, time = q.popleft()
        
        if x == K: 
            print(time)
            print(*get_path(x))
            return

        for new_x in (x+1, x-1, 2*x):
            if in_range(new_x) and not visited[new_x]:
                visited[new_x] = True
                path[new_x] = x
                q.append((new_x, time+1))

bfs()