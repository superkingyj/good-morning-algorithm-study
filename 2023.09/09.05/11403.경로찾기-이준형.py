from sys import stdin

input = stdin.readline
n = int(input())
graph = []

for _ in range(n):
    rows = list(map(int, input().split()))
    graph.append(rows)
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[k][j]==1 and graph[i][k]==1:
                graph[i][j]=1

for i in range(n):
    print(*graph[i], sep=" ")