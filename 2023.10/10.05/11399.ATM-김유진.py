import sys

N = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
times.sort()
result = 0
tmp = 0

for i in range(N):
    if i == 0: 
        result += times[i]
        tmp = times[i]
    else: 
        result += (tmp + times[i])
        tmp += times[i]
        

print(result)