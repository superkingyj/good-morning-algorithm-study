import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)

N = int(input())
nodes = defaultdict(list)

for i in range(N-1):
    a, b, c = map(int, input().split())
    nodes[a].append([b,c])
    nodes[b].append([a,c])
    
visited = [0] * (N+1)
def dfs(node, weight):
    visited[node] += weight
    for i, j in nodes[node]:
        if not visited[i]:
            dfs(i,weight+j)

dfs(1, 0)

idx = visited.index(max(visited))

visited = [0]*(N+1)

dfs(idx, 0)

print(max(visited))