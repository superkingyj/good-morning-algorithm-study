import sys

N = int(sys.stdin.readline())
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
DP = [[1001] * 3 for _ in range(N)]

DP[0][0] = arr[0][0]
DP[0][1] = arr[0][1]
DP[0][2] = arr[0][2]

for i in range(1, N):
    DP[i][0] = arr[i][0] + min(DP[i-1][1], DP[i-1][2])
    DP[i][1] = arr[i][1] + min(DP[i-1][0], DP[i-1][2])
    DP[i][2] = arr[i][2] + min(DP[i-1][0], DP[i-1][1])

# print(DP)
print(min(DP[-1]))