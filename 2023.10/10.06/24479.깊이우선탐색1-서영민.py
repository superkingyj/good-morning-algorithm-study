import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
count = 1    

def dfs(node):
    global count
    
    visited[node] = count
    
    graph[node].sort()
    for n in graph[node]:
        if not visited[n]:
            count += 1
            dfs(n)

dfs(R)

print(*visited[1:], sep='\n')