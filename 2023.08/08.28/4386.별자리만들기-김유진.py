import sys, math

N = int(sys.stdin.readline())
pos = [tuple(map(float, sys.stdin.readline().split())) for _ in range(N)]
parent = [i for i in range(N)]
edges = []
result = 0

def find(parent, x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB



for i in range(N-1):
    for j in range(i+1, N):
        a = abs(pos[j][0] - pos[i][0])
        b = abs(pos[j][1] - pos[i][1])
        dist = math.sqrt((a*a) + (b*b))
        edges.append((dist, i, j))
    
edges.sort()

for w, v1, v2 in edges:
    if find(parent, v1) != find(parent, v2):
        union(parent, v1, v2)
        result += w

print(result)        