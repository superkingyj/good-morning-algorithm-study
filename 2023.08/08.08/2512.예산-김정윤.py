import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline())

left = 0
right = max(arr)
result = 0

while left <= right:
    mid = (left + right) // 2
    sum = 0
    
    for i in arr:
        if mid < i:
           sum += mid
        else:
            sum += i
            
    if sum <= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)

