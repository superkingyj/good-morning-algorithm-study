import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
min_sub = sys.maxsize
result = []

left, right = 0, N-1
while left < right:
    sub = abs(arr[left] + arr[right])
    
    if sub < min_sub:
        min_sub = sub
        result = [arr[left], arr[right]]
    
    if sub == 0:
        result = [arr[left], arr[right]]
        break
    elif arr[left] + arr[right] > 0: right -= 1
    else: left += 1

print(*result)