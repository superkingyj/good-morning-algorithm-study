import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    count = 0
    arr = set([])
    arr2 = set([])

    for i in range(N):
        arr.add(int(sys.stdin.readline()))
    for i in range(M):
        arr2.add(int(sys.stdin.readline()))
    
    count = len(arr.intersection(arr2))

    print(count)