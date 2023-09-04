import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for k in range(N):
        for j in range(N):
            if arr[k][i] == 1 and arr[i][j] == 1:
                arr[k][j] = 1

for i in arr:
    print(*i)
                