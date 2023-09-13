import sys
from itertools import combinations

# 이항계수 N개중에 K개를 고르는 경우의 수 (nCk)
# 파스칼의 삼각형: nCr = (n-1)Ck + (n-1)C(k-1)

N, K = map(int, sys.stdin.readline().split())
DP = [[1] * (N+1) for _ in range(N+1)]

for i in range(2, N+1):
    for j in range(1, i):
        DP[i][j] = DP[i-1][j-1] + DP[i-1][j]

print(DP[N][K]%10007)


