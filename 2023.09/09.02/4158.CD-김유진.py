import sys

while True:
    N, M = map(int, sys.stdin.readline().split())

    if N == 0 and M == 0:
        break

    SK = set(int(sys.stdin.readline()) for _ in range(N))
    SY = set(int(sys.stdin.readline()) for _ in range(N))
    print(len(SK.intersection(SY)))
