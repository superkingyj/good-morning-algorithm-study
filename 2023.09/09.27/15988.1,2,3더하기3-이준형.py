from sys import stdin
input = stdin.readline

T = int(input())
dp = [1,2,4,7]
for i in range(4,1000001):
    dp.append((dp[i-1]+dp[i-2]+dp[i-3])%1000000009)

for _ in range(T):
    N = int(input())
    print(dp[N-1])