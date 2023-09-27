import sys

N, K = map(int, sys.stdin.readline().split())

cnt = 0

while bin(N).count('1') > K:
    N += 1
    cnt += 1 

print(cnt)