import sys
from collections import defaultdict, deque

N, M, R = map(int, sys.stdin.readline().split())
visited = [0] * (N + 1)
graph = defaultdict(list)
order = 1

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs():
    global order
    q = deque()
    q.append((R))
    visited[R] = order
    
    while q:
        v = q.popleft()
        
        graph[v].sort(reverse=True)
        for _v in graph[v]:
            if not visited[_v]:
                order += 1
                visited[_v] = order
                q.append(_v)

bfs()

for order in visited[1:]:
    print(order)