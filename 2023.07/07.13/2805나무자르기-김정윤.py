import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    
    for i in arr:
        if i > mid:
            cnt += i - mid    
    if cnt >= M:
          start = mid + 1
    else:
          end = mid - 1
print(end)