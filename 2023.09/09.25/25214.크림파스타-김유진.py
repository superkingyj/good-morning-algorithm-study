import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
min_val = sys.maxsize
DP = [0] * N

for i in range(N):
    if i == 0: 
        DP[i] = 0 
        min_val = arr[i]
        continue
    
    min_val = min(min_val, arr[i])
    DP[i] = max(DP[i-1], arr[i] - min_val)

print(*DP)