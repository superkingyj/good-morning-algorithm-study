from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int ,input().split())

board = [0]*101
for _ in range(N+M):
    u, v = map(int, input().split())
    board[u] = v

q = deque()
q.append((0,0))
    
while q:
    now, cnt = q.popleft()
    
    if now == 100:
        print(cnt)
        break
    
    for i in range(6, -1, -1):
        if now+i <= 100 and board[now+i] >= 0:
            if board[now+i] > 0:
                temp = board[now+i]
                board[now+i] = -1
                now = temp
            elif now+i <= 100:
                board[now+i] = -1
                now += i
            q.append((now, cnt+1))
        