#점화식
n = int(input())

dp = [[0,0,0] for _ in range(n)]
dp[0] = [1,1,1]

if n == 1:
    print(dp[1])
else:
    for i in range(2, n+1):
        dp[i] = dp[i-2] + (dp[i-1]*2 )
        dp[i] %=9901
    print(dp[n])