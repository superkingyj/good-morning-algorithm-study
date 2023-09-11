import sys
import heapq
from collections import defaultdict

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(M):
    u, v, w  = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    
start, end = map(int, sys.stdin.readline().split())

def dijkstra(start, end):
    q  = [(0, start)]
    dist = defaultdict(int)
    
    while q:
        weight, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = weight
            for m, x in graph[node]:
                alt = weight + x
                heapq.heappush(q, (alt, m))
    
    print(dist)
    return dist[end]

print(dijkstra(start, end))
        