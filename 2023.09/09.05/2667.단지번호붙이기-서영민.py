N = int(input())

apart = []
for i in range(N):
    apart.append(list(map(int, input())))
    
visited = [[0] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and apart[nx][ny] == 1:
            count += 1
            dfs(nx, ny)
    

res = []
for i in range(N):
    for k in range(N):
        if not visited[i][k] and apart[i][k] == 1:
            count = 1
            dfs(i, k)
            res.append(count)
res.sort()
print(len(res), *res, sep='\n')