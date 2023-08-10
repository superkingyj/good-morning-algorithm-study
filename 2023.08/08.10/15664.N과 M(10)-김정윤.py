from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
for i in sorted(set(combinations(sorted(map(int,sys.stdin.readline().split())), M))):
    print(*i)