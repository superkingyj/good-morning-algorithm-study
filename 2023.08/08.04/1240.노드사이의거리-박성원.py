import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = {}

# 그래프 만들기
for _ in range(n-1) :
    node, next_node, distance = map(int, input().split())
    graph[node] = (next_node, distance)
    graph[next_node] = (node, distance)




def bfs(start, find) :
    queue = deque()
    queue.append((start, 0))
    visited = [False] * (n+1)
    visited[start] = True

    while queue :
        v, d = queue.popleft()

        if v == find :
            return d
        
        for i in graph[v] :
            if not visited[i] :
                visited[i] = True
                queue.append((i, d))

# 탐색하기
for _ in range(m) :
    a, b = map(int, input().split())
    print(bfs(a,b))