from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

N, M, V = map(int, sys.stdin.readline().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
dfs_visited = [0] * (N + 1)
bfs_visited = [0] * (N + 1)
dfs_result = []
bfs_result = []

def dfs(startNode):
    dfs_visited[startNode] = 1
    dfs_result.append(startNode)
    for i in range(1, N + 1):
        if dfs_visited[i] == 0 and graph[startNode][i] == 1:
            dfs(i)

def bfs(startNode):
    q = deque()
    q.append(startNode)
    bfs_visited[startNode] = 1
    while q:
        startNode = q.popleft()
        bfs_result.append(startNode)
        for i in range(1, N + 1):
            if bfs_visited[i] == 0 and graph[startNode][i] == 1:
                bfs_visited[i] = 1
                q.append(i)

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start][end] = graph[end][start] = 1
    
dfs(V)
print(*dfs_result)
bfs(V)
print(*bfs_result)