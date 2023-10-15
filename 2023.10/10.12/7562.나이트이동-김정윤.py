import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    q = deque()
    q.append((now_x, now_y))
    while q:
        x, y = q.popleft()
        if x == goto_x and y == goto_y:
            return arr[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < l and ny >= 0 and ny < l and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

T = int(sys.stdin.readline())
for i in range(T):
    l = int(sys.stdin.readline())
    arr = [[0] * l for _ in range(l)]
    now_x, now_y = map(int, sys.stdin.readline().split())
    goto_x, goto_y = map(int, sys.stdin.readline().split())
    arr[now_x][now_y] = 1
    print(bfs())