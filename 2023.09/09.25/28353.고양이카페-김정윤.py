import sys

N, K = map(int, sys.stdin.readline().split())
weight = sorted(list(map(int, sys.stdin.readline().split())))
count = 0

start, end = 0, N - 1

while start < end:
    temp = weight[start] + weight[end]
    if temp <= K:
        end -= 1
        start += 1
        count += 1
    else:
        end -= 1
        
print(count)

