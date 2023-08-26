import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

distance = [-1] * 100001
distance[N] = 0

temp = 0
queue = deque([N])
count = 0

while queue:
    result = queue.popleft()
    if result == K:
        temp = distance[result]
        count += 1
        continue
    
    for i in (result - 1, result + 1, result * 2):
        if 0 <= i < 100001:
            if distance[i] == -1 or distance[i] == distance[result] + 1:
                queue.append(i)
                distance[i] = distance[result] + 1
                
print(temp)
print(count)