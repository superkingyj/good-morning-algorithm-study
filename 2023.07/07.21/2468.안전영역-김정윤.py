import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

def dfs(y, x, i):
    for m in range(4):
        ny = y + dy[m]
        nx = x + dx[m]
        if (ny >= 0 and nx >= 0 and ny < N and nx < N and visited[ny][nx] == 0 and arr[ny][nx] > i):
            visited[ny][nx] = 1
            dfs(ny, nx, i)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt_temp = []


for i in range(101):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if arr[j][k] > i and visited[j][k] == 0:
                cnt += 1
                dfs(j, k, i)
                visited[j][k] = 1
    cnt_temp.append(cnt)
print(max(cnt_temp))