import sys

_input = sys.stdin.readline

n, m = map(int, _input().split())

graph = [[] for _ in range(n+1)] 

def dfs(node, distance, target):
    visited[node] = 1
    
    if node == target:
        return distance
    
    for next_node in graph[node]:

        if not visited[next_node[0]]:
            result = dfs(next_node[0], distance+next_node[1], target)
            if result != -1:
                return result
    return -1

for i in range(n-1):
    a, b, c = map(int, _input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    
for _ in range(m):
    na , nb = map(int, _input().split())
    visited = [0 for _ in range(n+1)]
    distance = dfs(na, 0, nb)
    print(distance)
    