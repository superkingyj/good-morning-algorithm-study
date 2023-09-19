import sys
from collections import defaultdict

def dfs(v, money):
    visited[v] = True
    
    if v == N:
        return
    
    for _v in graph[v][2]:
        if visited[_v]: continue
        if graph[_v][0] == "E":
            dfs(_v, money)
        elif graph[_v][0] == "L":
            if money < graph[_v][1]: dfs(_v, graph[_v][1])
            else: dfs(_v, money)
        else:
            if money < graph[_v][1]: continue
            else: dfs(_v, money-graph[_v][1])

while True:
    N = int(sys.stdin.readline())    
    if N == 0: break
    
    graph = defaultdict(list)
    visited = [False] * (N+1)

    for i in range(1, N+1):
        input = list(sys.stdin.readline().rstrip().split())
        input.pop()
        graph[i] = (input[0], int(input[1]), list(map(int, input[2:])))
    
    if graph[1] != "T": 
        dfs(1, graph[1][1])

    if visited[N]: print("Yes")
    else: print("No")