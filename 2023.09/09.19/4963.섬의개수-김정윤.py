import sys
sys.setrecursionlimit(10 ** 6)

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]

def dfs(x, y):
    arr[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < h and ny >= 0 and ny < w and arr[nx][ny] == 1:
            arr[nx][ny] = 0
            dfs(nx, ny)
            
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    count = 0
   
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                dfs(i, j)
                count += 1
                
    print(count)
