from sys import stdin
from collections import deque
input = stdin.readline
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, C, N = map(int, input().split())

bomb = []
for _ in range(R):
    bomb.append(list(input().rstrip()))
    
def bfs():
    while queue:
        x,y = queue.popleft()
        bomb[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and bomb[nx][ny] == 'O':
                bomb[nx][ny] = '.'

for time in range(1,N+1):
    
    if time == 1:
        for i in range(R):
            for j in range(C):
                if bomb[i][j] == 'O':
                    queue.append((i, j))
    elif time%2 == 1:
        bfs()
        for i in range(R):
            for j in range(C):
                if bomb[i][j] == 'O':
                    queue.append((i, j))
    else:
        bomb = [['O']*C for _ in range(R)]

for i in bomb:
    print(*i,sep='')