import sys
input = sys.stdin.readline

n = int(input())
li = [0] + [int(input()) for _ in range(n)]

dp = [0]*(n+1)
dp[1] = li[1]
if n>1 :
    dp[2] = li[1]+li[2]

for i in range(3, len(dp)):
    dp[i] = max(li[i]+dp[i-2], li[i]+li[i-1]+dp[i-3], dp[i-1])

print(max(dp))

