import sys
sys.setrecursionlimit(10 ** 6)

T = int(sys.stdin.readline())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < M and ny >= 0 and ny < N:
            if arr[ny][nx] == 1:
                arr[ny][nx] = -1
                dfs(nx, ny) 
    

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    result = 0
    
    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    
    for l in range(M):
        for o in range(N):
            if arr[o][l] == 1:
                dfs(l, o)
                result += 1
    print(result)