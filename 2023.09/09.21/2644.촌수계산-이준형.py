from sys import stdin
from collections import deque
input = stdin.readline

def bfs(a):
    queue.append(a)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = visited[x]+1
                queue.append(i)
    
n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
queue = deque()
visited = [0] * (n+1)
bfs(a)


print(visited[b] if visited[b] > 0 else -1)