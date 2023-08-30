from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (N+1)
res = []   
def dfs(node):
    res.append(node)
    visited[node] = 1
    nexts = graph[node]
    nexts.sort()
    for next in nexts:
        if not visited[next]:
            dfs(next)
dfs(V)
print(*res)

res = []
visited = [0] * (N+1)            
def bfs():
    q = deque()
    q.append(V)
    visited[V] = 1
    while q:
        n = q.popleft()
        res.append(n)
        nexts = graph[n]
        nexts.sort()
        for next in nexts:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
bfs()
print(*res)