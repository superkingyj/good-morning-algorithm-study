import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(N-1):
    v1, v2, d = map(int, sys.stdin.readline().split())
    graph[v1].append((v2, d))
    graph[v2].append((v1, d))
    
def bfs(start, end):
    q = deque()
    visisted = [True] + [False] * N
    
    visisted[start] = True
    q.append((start, 0))
    result = 0
    
    while q:
        v, d = q.popleft()
        
        if v == end:
            result = d
            break
        
        for _v, _d in graph[v]:
            if not visisted[_v]:
                visisted[_v] = True
                q.append((_v, d+_d))

    return result

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(bfs(start, end))