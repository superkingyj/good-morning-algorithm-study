import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = [-1] * N

for i in range(N-2, -1, -1):
    if arr[i] == arr[i+1]:
        result[i] = result[i+1]
    else:
        result[i] = i+2
print(*result)   