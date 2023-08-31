import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for i in range(N - 1):
    startNode, EndNode = map(int, sys.stdin.readline().split())
    graph[startNode].append(EndNode)
    graph[EndNode].append(startNode)
    
def find(node):
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = node
            find(i)
            
find(1)

for i in range(2, N + 1):
    print(visited[i])
    