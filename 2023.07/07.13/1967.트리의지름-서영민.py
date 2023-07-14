import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)

N = int(input())
nodes = defaultdict(list)

max_length = 0
max_idx = 0

for i in range(N-1):
    a, b, c = map(int, input().split())
    nodes[a].append([b,c])
    nodes[b].append([a,c])
    
visited = [0] * (N+1)

def dfs(node, weight):
    global max_length, max_idx
    
    if max_length < weight:
        max_length = weight
        max_idx = node
        
    visited[node] = 1
    
    for i, j in nodes[node]:
        if not visited[i]:
            dfs(i,weight+j)

dfs(1, 0)

visited = [0]*(N+1)

max_length = 0
dfs(max_idx, 0)

print(max_length)