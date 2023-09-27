import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
visited = [0] * (N + 1)

graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)    

for i in range(N + 1):
    graph[i].sort(reverse=True)
    
    
def bfs(graph, R, visited):
    q = deque([R])
    visited[R] = 1
    count = 2
    
    while q:
        R = q.popleft()
        
        for i in graph[R]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = count
                count += 1
                
bfs(graph, R, visited)

for i in range(1, N + 1):
    print(visited[i])