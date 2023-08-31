import sys

V, E = map(int, sys.stdin.readline().split())
dist = [[sys.maxsize] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    dist[A][A] = 0
    dist[A][B] = C


def floyd_warshall():
    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


result = sys.maxsize
floyd_warshall()
for i in range(1, V + 1):
    for j in range(1, V + 1):
        if i == j:
            continue
        result = min(result, dist[i][j] + dist[j][i])

print(result if result != sys.maxsize else -1)
