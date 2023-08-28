# https://www.acmicpc.net/problem/4386
# https://bbbyung2.tistory.com/80

import math

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [i for i in range(n+1)]
stars = [list(map(float, input().split())) for _ in range(n)]

edges = []
result = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))
edges.sort()

for edge in edges :
    cost, x, y = edge

    if find_parent(x) != find_parent(y) :
        union_parent(x, y)
        result += cost

print(round(result, 2))