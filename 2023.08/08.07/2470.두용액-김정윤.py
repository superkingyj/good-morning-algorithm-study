import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
left = 0
right = N - 1
result = sys.maxsize

while left < right:
    temp = arr[left] + arr[right]
    if abs(temp) <= abs(result):
        result = temp
        temp_left = left
        temp_right = right
        
    if temp < 0:
        left += 1
    else:
        right -= 1
print(arr[temp_left], arr[temp_right])
    
    
     