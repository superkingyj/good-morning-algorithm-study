n = int(input())

students = list(map(int,input().split()))
dp = [0 for _ in range(1+n)]

for i in range(n+1):
    max_num = 0
    min_num = 10001
    for j in range(i,0,-1):
        max_num = max(max_num,students[j-1])
        min_num = min(min_num,students[j-1])
        dp[i] = max(dp[i], max_num - min_num + dp[j - 1])

print(dp[n])