import sys

N = int(sys.stdin.readline())
dp = [[0] * 3 for _ in range(N+1)]

# 왼칸에 사자가 있는 경우의 수
dp[1][0] = 1
# 오른칸에 사자가 있는 경우의 수
dp[1][1] = 1
# 사자가 있는 경우의 수
dp[1][2] = 1

for i in range(2, N+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%9901

print(sum(dp[-1])%9901)