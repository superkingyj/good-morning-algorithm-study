from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
board, res, cnt = [],[],1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()

for _ in range(n):
    board.append(list(map(int,input().rstrip())))


def bfs(x,y):
    global cnt
    board[x][y] = 0
    q.append((x,y))
    while q:
        cur = q.popleft()
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            
            if 0<= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                board[nx][ny] = 0
                cnt +=1
                q.append((nx,ny))
                

for a in range(n):
    for b in range(n):
        if board[a][b] == 1:
            cnt = 1
            bfs(a,b)
            res.append(cnt)

print(len(res))
res.sort()
print(*res, sep='\n')