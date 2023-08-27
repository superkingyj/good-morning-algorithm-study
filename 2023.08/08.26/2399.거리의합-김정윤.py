import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
result = 0
arr.sort()

for i in range(N):
    result += arr[i] * 2 * (2 * i - N + 1)
    
print(result)