from collections  import deque
import sys
input = sys.stdin.readline

dx = [-2,-1,2,1,-2,-1,2,1]
dy = [-1,-2,-1,-2,1,2,1,2]

def bfs(board, sx,sy, ex,ey):
    q = deque()
    q.append((sx, sy, 0))
    board[sx][sy] = 1
    
    while q:
        x, y, cnt = q.popleft()
        
        if x == ex and y == ey:
            print(cnt)
            break
        for a, b in zip(dx, dy):
            nx, ny = x+a, y+b
            if 0 <= nx < len(board) and 0 <= ny < len(board) and not board[nx][ny]:
                board[nx][ny] = 1
                q.append((nx, ny, cnt+1))

T = int(input())

for _ in range(T):
    length = int(input())
    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())
    
    board = [[0]*length for _ in range(length)]
    bfs(board, s_x, s_y, e_x, e_y)