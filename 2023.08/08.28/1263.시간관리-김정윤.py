import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    T, C = map(int, sys.stdin.readline().split())
    arr.append((T, C))
    
arr.sort(key=lambda T: T[1], reverse=True)

time = arr[0][1] - arr[0][0]
for i in range(1, N):
    if time > arr[i][1]:
        time = arr[i][1] - arr[i][0]
        
    else:
        time -= arr[i][0]
        
if time < 0:
    print(-1)
else:
    print(time)