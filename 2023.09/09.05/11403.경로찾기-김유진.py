import sys

N = int(sys.stdin.readline())
dist = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] == 1 or (dist[i][k] == 1 and dist[k][j] == 1):
                    dist[i][j] = 1


floyd_warshall()
for i in range(N):
    print(*dist[i])
