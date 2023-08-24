import sys

N = int(sys.stdin.readline())
student = [0] + list(map(int, sys.stdin.readline().split()))
DP = [0] * (N + 1)

for i in range(N + 1):
    max_val = 0
    min_val = 10001

    for j in range(i, 0, -1):
        max_val = max(max_val, student[j])
        min_val = min(min_val, student[j])
        DP[i] = max(DP[i], max_val - min_val + DP[j - 1])

print(DP[-1])
