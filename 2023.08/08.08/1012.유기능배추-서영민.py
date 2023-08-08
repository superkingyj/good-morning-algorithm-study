import sys
sys.setrecursionlimit(10 ** 6)

input_ = sys.stdin.readline

t = int(input_())


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y):
    
    visited[x][y] = 1
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if board[nx][ny] == 1:
                dfs(nx, ny)
            
for _ in range(t):
    count = 0
    m, n, k = map(int, input_().split())
    board = [[0]*m for _ in range(n)]
    for i in range(k):
        bx, by = map(int, input_().split())
        board[by][bx] = 1
    count = 0
    visited = [[0]*m for _ in range(n)]
    for k in range(n):
        for a in range(m):
            if board[k][a] == 1 and not visited[k][a]:
                dfs(k, a)
                count += 1
    print(count)