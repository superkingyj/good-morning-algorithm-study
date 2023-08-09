import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(N + 1)]
distance = [-1] * (N + 1)
result = []

for i in range(M):
    startNode, EndNode = map(int, sys.stdin.readline().split())
    arr[startNode].append(EndNode)

distance[X] = 0

queue = deque([X])
while queue:
    cur = queue.popleft()
    for nextNode in arr[cur]:
        if distance[nextNode] == -1:
            # 거리에다가 1 더해줌
            distance[nextNode] = distance[cur] + 1
            queue.append(nextNode)

                
for i in range(len(distance)):
    # K와 같은 경우 append로 추가해줌
    if distance[i] == K:
        result.append(i)


if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)
    