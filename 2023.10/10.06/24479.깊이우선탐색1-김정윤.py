import sys
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().split())
count = 1
def dfs(node):
    global count
    visited[node] = count
    for i in graph[node]:
        if visited[i] == 0:
            count += 1
            dfs(i)
    

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in graph:
    i.sort()
    

dfs(R)
for i in range(1, N + 1):
    print(visited[i])