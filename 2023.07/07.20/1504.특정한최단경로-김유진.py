import sys
import heapq
from collections import defaultdict

N, E = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

V1, V2 = map(int, sys.stdin.readline().split())

def djikstra(start):
    q = [(0, start)]
    dist = [sys.maxsize] * (N+1)
    dist[start] = 0
    
    while q:
        time, node = heapq.heappop(q)
        
        if dist[node] < time: 
            continue
        
        for _node, _time in graph[node]: 
            
            alt = time + _time
            if dist[_node] > alt:
                dist[_node] = alt
                heapq.heappush(q, (alt, _node))
    
    return dist


dist_from_1 = djikstra(1)
dist_from_V1 = djikstra(V1)
dist_from_V2 = djikstra(V2)

v1_dist = dist_from_1[V1] + dist_from_V1[V2] + dist_from_V2[N]
v2_dist = dist_from_1[V2] + dist_from_V2[V1] + dist_from_V1[N]

result = min(v1_dist, v2_dist)

print(result if result < sys.maxsize else -1)