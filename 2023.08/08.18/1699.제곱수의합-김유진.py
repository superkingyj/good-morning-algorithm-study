import sys
 
N = int(sys.stdin.readline())

DP = [num for num in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i):
        if j*j > i: break
        DP[i] = min(DP[i], DP[i-j*j]+1)

print(DP[-1])    