import sys

N = int(sys.stdin.readline())

# N이 0일때와 1일때 각각 방법이 1개와 3개라서 1, 3 미리 저장
dp = [1, 3] + [0] * (N - 1)

for i in range(2, N + 1):
    # 2번째 전 값 + 1번째 전 값에 곱하기 2 하면 결과 나옴
    dp[i] = (dp[i - 2] + dp[i - 1] * 2) % 9901
    
print(dp[N])