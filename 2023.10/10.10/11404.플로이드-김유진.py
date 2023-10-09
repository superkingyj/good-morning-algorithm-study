import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
dist = [[sys.maxsize] * (N+1) for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    dist[A][A] = 0
    dist[A][B] = min(dist[A][B], C)

def floyd_warshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

floyd_warshall()
for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == sys.maxsize: print(0, end = " ")
        else: print(dist[i][j], end = " ")
    print()