import sys
from collections import deque, defaultdict

N, K = map(int, sys.stdin.readline().split())
visited = [-1] * 200001

def in_range(x):
    return 0 <= x <= 200000

def bfs():
    q = deque()
    visited[N] = 0
    q.append(N)
    cnt = 0

    while q:
        x = q.popleft()
        
        if x == K: 
            cnt += 1 
            continue
        
        for new_x in (x+1, x-1, 2*x):
            if not in_range(new_x): continue
            if visited[new_x] == -1 or visited[new_x] >= visited[x]+1:
                visited[new_x] = visited[x] + 1
                q.append(new_x)
    
    return cnt

cnt = bfs()
print(visited[K])
print(cnt)