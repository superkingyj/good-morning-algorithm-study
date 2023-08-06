import sys
import heapq
from collections import defaultdict

V, E = map(int, sys.stdin.readline().split())
S = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = [(0, start)]
    dist = defaultdict(int)

    while q:
        weight, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = weight
            for m, x in graph[node]:
                alt = weight + x
                heapq.heappush(q, (alt, m))
    
    return dist

dist = dijkstra(S)

for i in range(1, V+1):
    print("INF") if i not in dist else print(dist[i])