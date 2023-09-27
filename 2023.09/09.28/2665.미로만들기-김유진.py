import sys
from collections import deque

N = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
target = []
DP = [[0] * N for _ in range(N)]

def init():
    global target
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "0":
                target.append((i, j))

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def bfs():
    q = deque()
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    DP[0][0] = 1
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            
            if not in_range(new_x, new_y): continue
            
            # 새로운 경로이면서
            if DP[new_x][new_y] == 0:
                # 백이라면
                if grid[new_x][new_y] == "1":
                    DP[new_x][new_y] = DP[x][y]
                    q.append((new_x, new_y))
                # 흑이라면
                else:
                    DP[new_x][new_y] = DP[x][y]+1
                    q.append((new_x, new_y))

            # 도달한 적 있는 곳이라면서
            else:
                # 백이라면
                if grid[new_x][new_y] == "1":
                    if DP[new_x][new_y] > DP[x][y]:
                        DP[new_x][new_y] = DP[x][y]
                        q.append((new_x, new_y))
                # 흑이라면
                else:
                    if DP[new_x][new_y] > DP[x][y]+1:
                        DP[new_x][new_y] = DP[x][y]+1
                        q.append((new_x, new_y))
    
    
bfs()
print(DP[-1][-1]-1)