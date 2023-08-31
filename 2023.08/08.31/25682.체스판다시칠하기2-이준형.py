from sys import stdin
input = stdin.readline

def miniboard(color):
    cnt = int(1e9)
    dp = [[0]*(M+1) for _ in range(N+1)]
    
    for i in range(N):
        for j in range(M):
            if (i+j)%2:
                val = board[i][j] == color
            else:
                val = board[i][j] != color
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + val
    
    for i in range(1, N-K+2):
        for j in range(1, M-K+2):
           cnt = min(cnt, dp[i+K-1][j+K-1] - dp[i+K-1][j-1] - dp[i-1][j+K-1] + dp[i-1][j-1])
                  
    return cnt


if __name__=="__main__":
    N, M, K = map(int, input().split())
    board = [input().rstrip() for _ in range(N)]
    
    B = miniboard('B')
    W = miniboard('W')
    
    print(min(B,W))