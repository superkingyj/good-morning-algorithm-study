import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    arr.sort()
    temp = arr[0] + arr[1]
    arr[0], arr[1] = temp, temp

print(sum(arr))