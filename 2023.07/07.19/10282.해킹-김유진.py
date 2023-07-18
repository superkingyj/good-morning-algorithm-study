import sys
import heapq
from collections import defaultdict

T = int(sys.stdin.readline())

def dijkstra(start):
    q = [(0, start)]
    dist = defaultdict(int)
    # cnt: 총 감염되는 컴퓨터 수
    # total_time: 마지막 컴퓨터가 감여되기까지 걸리는 시간
    
    while q:
        time, node = heapq.heappop(q)
        
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(q, (alt, v))
    
    # print(dist)
    cnt = len(dist.keys())
    total_time = max(dist.values())
    return cnt, total_time
    

for _ in range(T):
    N, D, C = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    visited = [True] + [False] * N
    
    for _ in range(D):
        A, B, S = map(int, sys.stdin.readline().split())
        # graph[A].append((B, S))
        graph[B].append((A, S))
        
    print(*dijkstra(C))