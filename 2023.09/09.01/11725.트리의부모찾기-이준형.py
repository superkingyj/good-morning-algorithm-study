from sys import stdin
from collections import deque
input = stdin.readline

def bfs():
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = x
                queue.append(i)


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int , input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

visited = [0]*(n+1)
bfs()

print(*visited[2:],sep='\n')

    
