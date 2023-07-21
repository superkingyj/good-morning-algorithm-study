import array
import heapq

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start_node):
    distances = array.array('i', [10**9] * (N + 1))
    distances[start_node] = 0

    q = [(0, start_node)]

    while q:
        distance, node = heapq.heappop(q)

        if distance > distances[node]:
            continue

        for new_node, weight in graph[node]:
            new_distance = distance + weight

            if new_distance < distances[new_node]:
                distances[new_node] = new_distance
                heapq.heappush(q, (new_distance, new_node))

    return distances

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

v1_v2_N_distance = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
v2_v1_N_distance = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

answer = min(v1_v2_N_distance, v2_v1_N_distance)

if answer >= 10**9:
    print(-1)
else:
    print(answer)