from sys import stdin

input = stdin.readline

def hap(M , dp):
    res = []
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        x1, y1 = x1 - 1, y1 - 1

        tmp = dp[x2][y2] - dp[x2][y1] - dp[x1][y2] + dp[x1][y1]
        res.append(tmp)

    return res


def main():
    N,M = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(N)]

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = board[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

    res = hap(M , dp)

    print(*res, sep='\n')
        
if __name__ == "__main__":
    main()