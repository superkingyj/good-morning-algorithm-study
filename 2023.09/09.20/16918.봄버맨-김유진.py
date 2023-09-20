import sys

R, C, N = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def init_bombs():
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                grid[i][j] = 2
            else:
                grid[i][j] = -1

def in_range(x, y):
    return 0 <= x < R and 0 <= y < C

def set_bombs():
    for i in range(R):
        for j in range(C):
            if grid[i][j] <= 0:
                grid[i][j] = 3
            else:
                grid[i][j] -= 1

def bomb_work():
    target = set()
    for i in range(R):
        for j in range(C):
            grid[i][j] -= 1
            if grid[i][j] == 0:
                    for k in range(4):
                        new_x, new_y = i+dx[k], j+dy[k]
                        if in_range(new_x, new_y): target.add((new_x, new_y))

    for i, j in target:
        grid[i][j] = -1

def print_grid():
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0: print("O", end = "")
            else: print(".", end = "")
        print()

init_bombs()
time = 1

while True:
    if time >= N: break

    # 3단계
    set_bombs()
    time += 1

    if time >= N: break

    # 4단계
    bomb_work()
    time +=1

    if time >= N: break

print_grid()