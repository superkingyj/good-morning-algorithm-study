import sys

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for i in range(n-1) :
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

print(graph)