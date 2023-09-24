야# https://www.acmicpc.net/problem/11051

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
# 초기 설정
d = [[0] * (n+1) for _ in range(n+1)]

for i in range(0, n+1) :
    d[i][1] = i
    d[i][0] = 1
    d[i][i] = 1

for i in range(2, n+1) :
    for j in range(1, i) :
        d[i][j] = d[i-1][j] + d[i-1][j-1]
        d[i][j] = d[i][j] % 10007

print(d[n][k])