import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

distance = [-1] * 100001
distance[N] = 0

queue = deque([N])

while queue:
    result = queue.popleft()
    
    if result == K:
        print(distance[result])
        break
    
    for i in (result - 1, result + 1, result * 2):
        if 0 <= i < 100001 and distance[i] == -1:
            if i == result * 2 and i != 0:
                distance[i] = distance[result]
                queue.appendleft(i)
            else:
                distance[i] = distance[result] + 1
                queue.append(i)
                