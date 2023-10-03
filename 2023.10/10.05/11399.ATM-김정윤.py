import sys

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
sum = 0
j = 1
for i in range(len(arr) -1 , -1, -1):
    sum += arr[i] * j
    j += 1
print(sum)