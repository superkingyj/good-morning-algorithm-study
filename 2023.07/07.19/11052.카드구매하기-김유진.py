import sys

N = int(sys.stdin.readline())
arr = [0] +  list(map(int, sys.stdin.readline().split()))

DP = [-sys.maxsize] * (N+1)
DP[0] = 0

for i in range(1, N+1):
    DP[i] = arr[i]
    for j in range(i):
        DP[i] = max(DP[i-j]+DP[j], DP[i])
        # print(DP[i])

print(DP[-1])
# print(DP) 