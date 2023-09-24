import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

cnt = 0
left, right = 0, N-1
while left < right:
    sum = arr[left] + arr[right]
    if sum <= K:
        cnt += 1
        left += 1
        right -= 1
    else:
        right -= 1

print(cnt)