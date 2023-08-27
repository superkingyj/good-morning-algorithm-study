import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

distance = [-1] * 100001
test = [-1] * 100001
distance[N] = 0
temp = 0
queue = deque([N])

while queue:
    result = queue.popleft()
    move = []
    if result == K:
        temp = distance[result]
        
        while result != N:
            move.append(result)
            result = test[result] 
        move.append(N)
        move.reverse()
        break
    
    for i in (result - 1, result + 1, result * 2):
        if 0 <= i < 100001:
            if distance[i] == -1 or distance[i] == distance[result] + 1:
                queue.append(i)
                distance[i] = distance[result] + 1
                test[i] = result
                
print(temp)
print(*move)