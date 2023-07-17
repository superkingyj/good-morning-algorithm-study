import sys
D, K = map(int, input().split())


def dp(a, b, d, k):
    DP = [0] * (d+1)
    DP[1] = a
    DP[2] = b
    for i in range(3, d+1):
        DP[i] = DP[i-1] + DP[i-2]
    if k == DP[-1]:
        return True
    else:
        return False
    
for i in range(1, 100001):
    for j in range(1, 100001):
        if dp(i, j, D, K):
            print(i)
            print(j)
            sys.exit()
