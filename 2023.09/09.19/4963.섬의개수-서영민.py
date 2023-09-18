import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

dx = [1,-1,0,0,-1,-1,1,1]
dy = [0,0,1,-1,-1,1,-1,1]

def dfs(x, y, m, n):
    
    if arr[x][y] == 1:
        arr[x][y] = 0
    
    for a, b in zip(dx, dy):
        nx, ny = x+a, y+b
        if 0 <= nx < n and 0<= ny <m and arr[nx][ny] == 1:
            dfs(nx, ny, m, n)

while True:
    m, n = map(int, input().split())
    
    if m == 0 and n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for k in range(m):
            if arr[i][k] == 1:
                dfs(i, k, m, n)
                cnt += 1
    print(cnt)
    
