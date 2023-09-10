import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        arr[i][j] = int(arr[i][j])

visited = [[0] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
q.append((0, 0))
visited[0][0] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                # 한칸씩 이동하면 1을 더해줌
                arr[nx][ny] = arr[x][y] + 1

print(arr[-1][-1])
                