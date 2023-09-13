import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
distance = [1000000000] * (N + 1)

for _ in range(M):
    startNode, EndNode, dist = map(int, sys.stdin.readline().split())
    graph[startNode].append((EndNode, dist))
    

# 방문하지 않은 노드면서 시작 노드와 최단 거리인 노드 반환
def get_least():
    min_value = 1000000000
    idx = 0
    for i in range(1, N + 1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            idx = i
    return idx


def dijkstra(start):

    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        if distance[i[0]] < i[1]:
            continue
        else:
            distance[i[0]] = i[1]
        

    for _ in range(N - 1):
        now = get_least()
        visited[now] = True
        for next in graph[now]:
            cost = distance[now] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                
                
first, End = map(int, sys.stdin.readline().split())

              
dijkstra(first)

if first == End:
    print(0)
    
else:
    print(distance[End])