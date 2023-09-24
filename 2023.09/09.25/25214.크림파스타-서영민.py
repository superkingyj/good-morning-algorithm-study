N = int(input())

arr = list(map(int, input().split()))

dp = [0] * N

min_value = arr[0]

dp[0] = 0

for i in range(1, N):
    dp[i] = max(dp[i-1], arr[i] - min_value)
    min_value = min(min_value, arr[i])
    
print(*dp)