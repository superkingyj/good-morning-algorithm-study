import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

result = [0]
minn = arr[0]
for i in range(1, N):
    
    temp = arr[i] - minn
    if temp > result[i - 1]:
        result.append(temp)
    else:
        result.append(result[i - 1])
        
    if arr[i] < minn:
        minn = arr[i]
        
print(*result)