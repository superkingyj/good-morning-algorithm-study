from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for i in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())

def bfs():
    q = deque()
    q.append((start, 0))
    visited = [sys.maxsize for _ in range(N+1)]
    visited[start] = 0
    
    while q:
        n, w = q.popleft()
        
        if visited[n] < w:
            continue
        
        for next_node, weight in graph[n]:
            
            if weight+w < visited[next_node]:
                visited[next_node] = weight + w
                q.append((next_node, weight + w))
    return visited[end]

res = bfs()
print(res)