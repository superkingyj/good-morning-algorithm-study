import sys

sys.setrecursionlimit(10*6)

input = sys.stdin.readline


n, r, q = map(int, input().split())

def dfs(node):

    visited[node] = 1
    
    next_nodes = graph[node]
    
    for next_node in next_nodes:
        if not visited[next_node]:
            visited[node] += dfs(next_node)
    return visited[node]       



graph = {}
result = 0

visited = [0 for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)
    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)    

dfs(r)
for _ in range(q):
    root = int(input())
    print(visited[root])

    
    
