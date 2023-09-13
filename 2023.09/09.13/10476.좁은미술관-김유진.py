import sys

N, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sys.stdin.readline()

if K == 0:
    ans = 0
    for L, R in arr:
        ans += L
        ans += R
    print(ans)
else:
    # i: 행 번호, j: 현재까지 닫힌 개수, k: L, R, both 순서대로 열림
    dp = [[[0, 0, 0] for _ in range(K+1)] for _ in range(N)]

    L, R = arr[0][0], arr[0][1]
    
    dp[0][1][0] = L
    dp[0][1][1] = R
    dp[0][0][2] = L+R

    for i in range(1, N):
        L = arr[i][0]
        R = arr[i][1]

        for j in range(K+1):
            if j >= 1:
                dp[i][j][0] = max(dp[i-1][j-1][0], dp[i-1][j-1][2]) + L
                dp[i][j][1] = max(dp[i-1][j-1][1], dp[i-1][j-1][2]) + R
            if i+1 != j:
                dp[i][j][2] = max(dp[i-1][j][0], dp[i-1][j][1], dp[i-1][j][2]) + L + R
        
    print(max(dp[-1][-1]))

"""
N행이 될수 있는 상태

0 - XO: 왼쪽만 닫힌 경우 -> 0이나 2가 와야함
1 - OX: 오른쪽만 닫힌 경우 -> 1이나 2가 와야함
2 - OO: 둘다 열려있는 경우 -> 0, 1, 2 전부 가능

DP[N][K][F] - N행까지 방을 K개 닫고 F상태일 때 가치의 최대합

DP[N][K][0] = max(DP[N-1][K-1][0], DP[N-1][K-1][2]) + arr[N][1] (왼쪽을 닫았으니 오른쪽의 가치를 더해줌)
DP[N][K][1] = max(DP[N-1][K-1][1], DP[N-1][K-1][2]) + arr[N][0] (오른쪽을 닫았으니 왼쪽의 가치를 더해줌)
DP[N][K][2] = max(DP[N-1][K-1][0], DP[N-1][K-1][1], DP[N-1][K-1][2]) + arr[N][0]+ arr[N][1] (왼쪽과 오른쪽의 가치를 더해줌)
"""