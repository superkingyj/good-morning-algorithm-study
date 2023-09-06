import sys
input = sys.stdin.readline

V, E = map(int, input().split())
INF = sys.maxsize
distance = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    distance[u][v] = w

for i in range(1, V+1):
    for k in range(1, V+1):
        for j in range(1, V+1):
             distance[k][j] = min(distance[k][j], distance[k][i]+distance[i][j])

res = INF
for i in range(1, V+1):
    res = min(res, distance[i][i])


print(-1) if res == INF else print(res)