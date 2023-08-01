import sys
from collections import deque

q = deque()
M, N, H = map(int, sys.stdin.readline().split())

box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

# 형식이 현재 [[[1, 1, 1][1,1,1]], [[1,1,1],[1,1,1]]] 의 형식으로 z,x,y 순서이다.

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            
            if nx >= 0 and ny >= 0 and nz >= 0 and nx < N and ny < M and nz < H:
                if box[nz][nx][ny] == 0:
                    # 다음 값이 0이면 현재 값에 1을 더해서 다음 값을 변경 이게 곧 날짜가 됨
                    box[nz][nx][ny] = box[z][x][y] + 1
                    # q에 다음 값들 추가
                    q.append((nz, nx, ny))

# 먼저 box에서 1인 값을 q에 추가
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append((i, j, k))
                
bfs()

Notvisited = False
result = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            # 박스 안에 0 즉, 익지 않은 토마토(0)가 존재한다면 Notvisited 가 True로 바뀜
            if box[i][j][k] == 0:
                Notvisited = True
            # 아까 bfs를 돌면서 날짜 값들을 정해놓은 것이 있기 때문에 거기서 최댓값을 구해줌
            result = max(result, box[i][j][k])

# True라면, 방문하지 않았기 때문에 -1 출력         
if Notvisited:
    print(-1)

#아니라면, 결과 값에서 1빼줌(원래 익어있던 첫 날 제외)
else:
    print(result - 1)
