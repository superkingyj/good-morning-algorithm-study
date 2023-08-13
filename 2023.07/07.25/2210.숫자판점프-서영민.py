import sys

input_ = sys.stdin.readline

board = list(list(input_().split()) for _ in range(5))

result = set()

def dfs(number, x, y):
    
    if len(number) == 6:
        result.add(number)
        return
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
        
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(number+board[x][y], nx, ny)



for i in range(5):
    for k in range(5):
        dfs("", i, k)

print(len(result))