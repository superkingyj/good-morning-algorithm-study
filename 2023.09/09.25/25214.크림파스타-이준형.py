from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0]*N
min_val = A[0]
for i in range(1,N):
    dp[i] = max(dp[i-1],A[i]-min_val)
    min_val = min(min_val,A[i])

print(*dp)