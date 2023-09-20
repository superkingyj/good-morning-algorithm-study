import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
grid = [[0] * N for _ in range(N)]

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    grid[x-1][y-1] = 1

L = int(sys.stdin.readline())
D = deque()

for _ in range(L):
    X, C = sys.stdin.readline().split()
    D.append((int(X), C))

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 오, 아, 왼, 위
time, x, y, dir = 0, 0, 0, 0
snake = deque()
snake.append([0, 0, 0])

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

flag = False
while True:
    # 몸길이를 늘려 머리를 다음칸으로 위치하기
    new_x, new_y = x+dx[dir], y+dy[dir]

    # 새로 움직인 곳이 벽일 경우 종료
    if not in_range(new_x, new_y): 
        flag = True
        break
    # 새로 움직인 곳이 자기자신일 경우 종료
    for _x, _y, _ in snake:
        if new_x == _x and new_y == _y: 
            flag = True
            break
    
    if flag: break
    
    # 이동한 칸에 사과가 있을 경우
    if grid[new_x][new_y] == 1:
        # 그 칸의 사과는 없어짐
        grid[new_x][new_y] = 0
        snake.append([new_x, new_y, dir])
        x, y = new_x, new_y
    # 이동한 칸에 사과가 없을 경우
    else:
        # 꼬리가 위치한 칸을 비움
        for i in range(len(snake)):
            if i == len(snake)-1: 
                _dir = dir
                # snake[i][2] = _dir
            else: _dir = snake[i+1][2]
            snake[i][0] = snake[i][0]+dx[_dir]
            snake[i][1] = snake[i][1]+dy[_dir]
            snake[i][2] = _dir
        x, y = new_x, new_y

    time += 1
    if D and D[0][0] == time:
        # D일 경우 오른쪽 90도 회전
        if D[0][1] == "D": dir = (dir + 1) % 4
        # L일 경우 왼쪽 90도 회전
        else: dir = (dir + 3) % 4
        D.popleft()

print(time+1)