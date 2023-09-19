import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [0] * (F + 1)
count = [0] * (F + 1)

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == G:
            return count[G]
        for i in (v+U, v - D):
            if i > 0 and i <= F and not visited[i]:
                visited[i] = 1
                count[i] = count[v] + 1
                q.append(i)
                
    if count[G] == 0:
        return "use the stairs"
    
print(bfs(S))