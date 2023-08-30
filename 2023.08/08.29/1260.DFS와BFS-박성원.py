# https://www.acmicpc.net/problem/1260

from collections import deque


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]


def dfs(v) :
    print(v, end=' ')
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            dfs(i)

def bfs(v) :
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue :
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in graph[now_Node] : 
            if not visited[i] :
                visited[i] = True
                queue.append(i)


visited = [False] * (n+1)


# 그래프 만들기
for _ in range(m) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 번호가 작은 노드부터 방문하기 위해 정렬
for i in range(n+1) :
    graph[i].sort()

dfs(v)
print()

visited = [False] * (n+1)
bfs(v)