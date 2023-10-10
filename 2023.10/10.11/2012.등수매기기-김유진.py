import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()

result = 0
for i in range(1, N + 1):
    result += abs(i - arr[i - 1])

print(result)
