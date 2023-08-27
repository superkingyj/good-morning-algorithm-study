import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []

def range_sum(x1, y1, x2, y2):
    
    total = 0
    for i in range(x1-1, x2):
        for k in range(y1-1, y2):
            total += board[i][k]
    return total


for _ in range(N):
    board.append(list(map(int, input().split())))
    
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(range_sum(x1, y1, x2, y2))


