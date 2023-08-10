import heapq
import sys
sys.setrecursionlimit(10**6)

input_ = sys.stdin.readline

n, m, k, x = map(int, input_().split())

inf = int(1e9)

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input_().split(" "))
    graph[a].append(b)
    graph[b].append(a)

distance = [inf]*(n+1)

    
def dijkstra(node):
    q = []
    heapq.heappush(q, (0, node))
    distance[node] = 0
    
    while q:
        dist, current_node = heapq.heappop(q)
        if distance[current_node] < dist:
            continue
        for next_node in graph[current_node]:
            next_distance = dist + 1
            if next_distance < distance[next_node]:
                distance[next_node] = next_distance
                heapq.heappush(q, (next_distance, next_node))
                
dijkstra(x)

flag = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i, end='\n')
        flag = True

if not flag:
    print(-1)