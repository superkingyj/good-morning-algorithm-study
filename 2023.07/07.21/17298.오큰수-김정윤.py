import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

temp = []
result = [-1] * N

for i in range(N):
    while True:
        if temp == [] or temp[-1][0] >= arr[i]:
            break
        result[temp.pop()[1]] = arr[i]
    temp.append([arr[i], i])
        
print(*result)