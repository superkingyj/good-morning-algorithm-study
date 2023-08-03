import sys

T = int(sys.stdin.readline())
arr = []

for i in range(T):
    N = int(sys.stdin.readline())
    count = 1
    arr = []
    for j in range(N):
        docu, t = map(int, sys.stdin.readline().split())
        arr.append((docu, t))
    arr.sort(key=lambda x: x[0])
    minta = arr[0][1]
    for j in arr:
        d, ta = j
        if minta > ta:
            count += 1
            minta = ta
    
    print(count)


