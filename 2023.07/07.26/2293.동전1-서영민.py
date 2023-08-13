import math

N, K = map(int ,input().split())

moneys = [map(int, input()) for _ in range(N)]

dp = [0 for _ in range(K+1)]


for i in moneys:
    for k in range(i, K+1):
        

