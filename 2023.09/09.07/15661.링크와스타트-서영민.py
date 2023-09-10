import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

res = sys.maxsize

values = []
for i in range(N-1):
    for k in range(i+1, N):
        value = arr[i][k] + arr[k][i]
        values.append(value)

for i in range(len(values)):
    for k in range(i+1, len(values)):
        res = min(res, abs(values[i]-values[k]))

print(values)    
print(res)