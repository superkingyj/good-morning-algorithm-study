import sys

n = int(sys.stdin.readline())

arr = []
dp = [0] * (3)

for i in range(3):
    arr.append(0)

for i in range(n):
    arr.append(int(sys.stdin.readline()))

# 고려해야하는 부분 0, 1 ,2 ,3 ,4, 5 까지 잔이 있다면
# 1 위치에서 안마신 경우 = dp[i] = dp[i - 3] + arr[i - 1] + arr[i]
# 2 위치에서 안마신 경우 = dp[i] = dp[i - 2] + arr[i]

for i in range(3, len(arr)):
    # 연속해서 두잔을 마시는 것과 중간 잔을 안마셨을 때 더 큰 값 비교
    temp = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i])
    # 3 위치에서 마시지 않는 경우, i -1 번째까지 탐색했을 때 마실 수 있는 최대 양 그대로 사용
    # 즉, 이전 temp 값과 현재 temp 값 중에 뭐가 더 큰지 비교
    dp.append(max(temp, dp[i - 1]))

print(dp[-1])