import sys

N, M, L = map(int, sys.stdin.readline().split())

arr = [0] + list(map(int, sys.stdin.readline().split())) + [L]
arr.sort()

start = 1
end = L - 1

result = 0

while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > mid:
            count += (arr[i] - arr[i - 1] - 1) // mid
    if count > M:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)