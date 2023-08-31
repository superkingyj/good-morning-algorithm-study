from collections import deque

import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parensts = [0 for _ in range(N+1)]    
def bfs():
    q = deque()
    q.append(1)
    parensts[1] = True
    
    while q:
        node = q.popleft()
        
        for i in graph[node]:
            if not parensts[i]:
                q.append(i)
                parensts[i] = node 

bfs()
for i in range(2, N+1):
    print(parensts[i])