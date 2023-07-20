#다익스트라
import sys
import heapq
input = sys.stdin.readline

#입출력
N, E = map(int,input().split())
edges = [[] for _ in range(N + 1)]

#리스트
for _ in range(E):
    a, b, c = map(int,sys.stdin.readline().rstrip().split())

    edges[a].append([b, c])
    edges[b].append([a, c])

v1, v2 = map(int,input().split())


#구현
#출발 노드로부터 모든 노드로 최단 거리 구함
#목표노드의 최단 거리 리턴
def dijkstra(start, end):
    route = [sys.maxsize]*(N+1)
    route[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)
        
        if route[node] < dist:
            continue
        
        for toNode, toDist in edges[node]:
            d = route[node] + toDist
            
            if d < route[toNode]:
                route[toNode] = d
                heapq.heappush(q, (d, toNode))

    return route[end]


# 1 > v1 > v2 > N
# 2 > v2 > v1 > N
route1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
route2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if route1 >= sys.maxsize and route2 >= sys.maxsize:
    print(-1)
else:
    print(min(route1, route2))