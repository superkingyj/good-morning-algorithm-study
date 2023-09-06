import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

board = [input().strip() for _ in range(N)]


def mini_board(color):
    prefix_sum = [[0]*(M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for k in range(1, M+1):
            if (i+k) % 2 == 0:
                if board[i-1][k-1] != color:
                    temp = 1
                else:
                    temp = 0
            else:
                if board[i-1][k-1] == color:
                    temp = 1
                else:
                    temp = 0
            prefix_sum[i][k] = prefix_sum[i-1][k] + prefix_sum[i][k-1] + temp - prefix_sum[i-1][k-1]
    
    res = sys.maxsize
    for i in range(1, N-K+2):
        for j in range(1, M-K+2):
            res = min(res, prefix_sum[i+K-1][j+K-1] - prefix_sum[i-1][j+K-1] -prefix_sum[i+K-1][j-1] + prefix_sum[i-1][j-1])
    return res

b = mini_board('B')
w = mini_board('W')

print(min(b, w))
        
    
