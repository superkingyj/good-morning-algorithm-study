import sys
input = sys.stdin.readline


def dfs(x, res, visited):
    
    visited[x] = 1
    parent = graph[x]
    if not visited[parent]:
        res.append(parent)
        dfs(parent, res, visited)
        
T = int(input())

for _ in range(T):
    N = int(input())
    graph = [0 for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        graph[v] = u
    x, y = map(int, input().split())
    
    res_x = []
    res_y = []
    
    visited = [0] * (N+1)
    visited2 = [0] * (N+1)
    dfs(x, res_x, visited)
    dfs(y, res_y, visited2)
    
    i = 1
    while res_x[-i] == res_y[-i]:
        i += 1
        if len(res_x) == i or len(res_y) == i:
            i += 1
            break
        
    print(res_x[-i + 1])