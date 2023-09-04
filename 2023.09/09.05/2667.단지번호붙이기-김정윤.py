import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

    
visited = [[False] * N for _ in range(N)]
cnt = 0
count = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]    

def dfs(x, y):
    visited[x][y] = True
    global cnt
    cnt += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == False:
            if arr[nx][ny] == '1':
                dfs(nx, ny)
                
            
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and arr[i][j] == '1':
            cnt = 0
            dfs(i, j)
            count.append(cnt)
            
            
print(len(count))
count.sort()
for i in count:
    print(i)