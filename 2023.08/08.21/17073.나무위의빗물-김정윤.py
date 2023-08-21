import sys

N, W = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

count = 0

for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(len(graph)):
    if i != 1 and len(graph[i]) == 1:
        count += 1

print(W / count)
