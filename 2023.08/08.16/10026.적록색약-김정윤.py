import sys
sys.setrecursionlimit (10 ** 6)

N = int(sys.stdin.readline())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * N for _ in range(N)]
count_n = 0
count = 0

def dfs(x, y):
    visited[x][y] = True
    temp = arr[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == False:
            if temp == arr[nx][ny]:
                dfs(nx, ny)
            
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i, j)
            count_n += 1
    
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visited = [[False] * N for _ in range(N)]     
            
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i, j)
            count += 1
            
print(count_n, count)