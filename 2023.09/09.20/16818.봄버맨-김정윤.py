import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

dx = [1, 0, -1 , 0]
dy = [0, 1, 0, -1]

def que():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                q.append((i, j))


def full():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = 'O'


def bfs():
    while q:
        x, y = q.popleft()
        arr[x][y] = '.'
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < R and ny >= 0 and ny < C:
                if arr[nx][ny] == 'O':
                    arr[nx][ny] = '.'
               
N -= 1

while N:
    q = deque()
    que()
    full()
    N -= 1
    if N == 0:
        break
    bfs()
    N -= 1
            
for i in arr:
    print(''.join(i))