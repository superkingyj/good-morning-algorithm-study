import sys
from collections import defaultdict, deque

N, M, K, X = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def bfs():
    q = deque()
    visited = [True] + [False] * N
    visited[X] = True
    q.append((X, 0))
    result = []
    
    while q:
        node, dist = q.popleft()
        
        if dist == K:
            result.append(node)
            
        for _node in graph[node]:
            if not visited[_node]:
                visited[_node] = True
                q.append((_node, dist+1))

    result.sort()
    return result

result = bfs()
if not result: print(-1)
else: 
    for node in result:
        print(node)