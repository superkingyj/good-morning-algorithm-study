import sys
from collections import defaultdict

sys.setrecursionlimit(150000)
N, M, R = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = [0]*(N+1) 
order = 1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  
    graph[b].append(a)  

def dfs(t):
    global order
    visited[t] = order
    graph[t].sort(reverse=True)
    for i in graph[t]:
        if visited[i] == 0:
            order += 1
            dfs(i)


dfs(R)
for i in range(1, N+1):
    print(visited[i])