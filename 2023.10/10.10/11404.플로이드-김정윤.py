import sys
INF = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a][b] = min(c, arr[a][b])

for i in range(1, n + 1):
    arr[i][i] = 0
    
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] == INF:
            print("0", end=" ")
        else:
            print(arr[i][j], end=" ")
    print()