import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
result = 0

for i in range(N):
    if arr[i] != (i + 1):
        result += abs(arr[i] - (i + 1))
        
print(result)