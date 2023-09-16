## 요거 틀린코드

from sys import stdin
input = stdin.readline

def max_value(N, k, gallery):
    dp = [[[0 for _ in range(3)] for _ in range(k+1)] for _ in range(N+1)]

    for n in range(1, N+1):
        dp[n][1][0] = gallery[n][1]
        dp[n][1][1] = gallery[n][0]
        dp[n][0][2] = gallery[n][1] + gallery[n][0]

    for n in range(2, N+1):
        for i in range(k+1):
            if i >= 1:
                dp[n][i][0] = max(dp[n-1][i-1][0], dp[n-1][i-1][2]) + gallery[n][1]
                dp[n][i][1] = max(dp[n-1][i-1][1], dp[n-1][i-1][2]) + gallery[n][0]

            if n != i:
                dp[n][i][2] = max(dp[n-1][i][0], dp[n-1][i][1], dp[n-1][i][2]) + gallery[n][0] + gallery[n][1]

    return max(dp[N][k][0], dp[N][k][1], dp[N][k][2])

while True:
    N, k = map(int, input().split())
    if N == 0 and k == 0:
        break
    gallery = [[0, 0] for _ in range(N+1)]

    for i in range(1, N+1):
        gallery[i] = list(map(int, input().split()))

    result = max_value(N, k, gallery)
    print(result)