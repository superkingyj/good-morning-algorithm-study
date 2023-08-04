import sys
n,m = map(int, sys.stdin.readline().split(" "))
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int, sys.stdin.readline().split(" "))
    graph[a].append([b,c])
    graph[b].append([a,c])

def bfs(start,end):
    root = [start]
    global n
    global graph
    visited = [0]*(n+1)
    way = [0]*(n+1)
    while root:
        k = root.pop(0)
        if k == end:
            break
        if visited[k] == 0:
            visited[k] = 1
            for i in graph[k]:
                root.append(i[0])
                way[i[0]] = way[k] + i[1]
    return way[end]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split(" "))
    print(bfs(a,b))