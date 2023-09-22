import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
board = [[0] * N for _ in range(N)]
turn = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(K):
    row, col = map(int, sys.stdin.readline().split())
    board[row - 1][col - 1] = 2
    
L = int(sys.stdin.readline())
for i in range(L):
    X, C = sys.stdin.readline().split()
    X = int(X)
    turn.append((X, C))

q = deque()
q.append((0, 0))
x, y = 0, 0
board[x][y] = 1
sec = 0 
direct = 0
    
def changedirect(t):
    global direct
    if t == 'L':
        direct = (direct - 1) % 4
    else:
        direct = (direct + 1) % 4
        
while True:
    sec += 1
    x += dx[direct]
    y += dy[direct]
    
    if x < 0 or x >= N or y < 0 or y >= N:
        break
    
    if board[x][y] == 2:
        board[x][y] = 1
        q.append((x, y))
        for i in range(L):
            if sec == turn[i][0]:
                changedirect(turn[i][1])
            
    elif board[x][y] == 0:
        board[x][y] = 1
        q.append((x, y))
        nx, ny = q.popleft()
        board[nx][ny] = 0
        for i in range(L):
            if sec == turn[i][0]:
                changedirect(turn[i][1])
            
    else:
        break
    
print(sec)
        
    