import sys
import math

N, K = map(int, sys.stdin.readline().split())

result = math.comb(N, K)

print(result % 10007)