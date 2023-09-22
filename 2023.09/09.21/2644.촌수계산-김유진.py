import sys
from collections import defaultdict

N = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
M = int(sys.stdin.readline())
visited = [0] * (N+1)
cnt = -1

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v, dist):
    visited[v] = dist
    for _v in graph[v]:
        if not visited[_v]:
            dfs(_v, dist+1)

dfs(start, 0)
if visited[end]: print(visited[end])
else: print(-1)
