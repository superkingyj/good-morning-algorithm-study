import sys
from collections import defaultdict, deque

N = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(N - 1):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (N + 1)
q = deque()
visited[1] = 1
q.append(1)

while q:
    v = q.popleft()
    for _v in graph[v]:
        if not visited[_v]:
            visited[_v] = v
            q.append((_v))

for i in range(2, N + 1):
    print(visited[i])
