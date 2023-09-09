from sys import stdin
from collections import deque
input = stdin.readline


def bfs(x,y):
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx,ny))
    return arr[n-1][m-1]

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

print(bfs(0,0))