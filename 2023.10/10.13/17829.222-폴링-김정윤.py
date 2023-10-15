import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def quad(arr, n):
    if n == 1:
        return arr[0][0]
    half = [[] for _ in range(n // 2)]
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            half[i//2].append(sorted([arr[i][j], arr[i][j + 1], arr[i + 1][j], arr[i + 1][j + 1]])[2])
    return quad(half, n // 2)

print(quad(arr, N))