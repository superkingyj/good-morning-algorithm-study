import sys
from collections import deque
def bfs():
    graph = [-1] * 100001
    graph[n] = 0
    queue = deque([n])

    while queue:
        target = queue.popleft()
        if target == k:
            return graph[target]
        for i in (target + 1, target - 1, target * 2):
            if 0 <= i <= 100000 and graph[i] == -1:
                if i == target * 2:
                    graph[i] = graph[target] 
                    queue.appendleft(i)
                else:
                    graph[i] = graph[target] + 1
                    queue.append(i)


n, k = map(int, sys.stdin.readline().split())
print(bfs())