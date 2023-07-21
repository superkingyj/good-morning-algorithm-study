import sys
sys.setrecursionlimit(100000)

N = int(input())

array = []
max_height = 0
for i in range(N):
    array.append(list(map(int, input().split())))
    _max = max(array[i])
    if max_height < _max:
        max_height = _max

def dfs(visited, x, y, target):
    visited[x][y] = True
    
    dx= [1,-1,0,0]
    dy= [0,0,1,-1]
    
    for i in range(4):
        for j in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if array[nx][ny] > target and not visited[nx][ny]:
                    dfs(visited, nx, ny, target)

result = 0
for i in range(max_height):
    visited = [[False]*N for _ in range(N)]
    count = 0
    
    for j in range(N):
        for k in range(N):
            if array[j][k] > i and visited[j][k] == False:
                dfs(visited, j, k, i)
                count += 1
    if result < count:
        result = count

print(result)