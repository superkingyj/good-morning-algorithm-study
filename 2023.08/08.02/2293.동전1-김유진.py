import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
DP = [0] * (K+1) #DP[i] = i원을 만들 수 있는 경우의 수
DP[0] = 1

for coin in coins:
    for money in range(coin, K+1):
        if money < coin: continue
        DP[money] += DP[money-coin]

print(DP[K])