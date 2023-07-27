import sys

N = int(sys.stdin.readline())

# 체력이 100이기 때문에 101 곱해줌 
dp = [[0] * 101 for _ in range(N + 1)]

hp = [0] + list(map(int, sys.stdin.readline().split()))
happy = [0] + list(map(int, sys.stdin.readline().split()))

# bottom-up 방식
for i in range(1, N + 1):
    for j in range(1, 101):
        
        if hp[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - hp[i]] + happy[i])

print(dp[N][99])