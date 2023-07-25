import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))
    
count = 0

for i in range(N - 1, 0, -1):
    if arr[i] > arr [i - 1]:
        continue
    elif arr[i] == arr[i - 1]:
        arr[i - 1] -= 1
        count += 1
    elif arr[i] < arr[i - 1]:
        count = count + (arr[i - 1] - arr[i]) + 1
        arr[i - 1] = arr[i - 1] - (arr[i - 1] - arr[i]) - 1
        

print(count)