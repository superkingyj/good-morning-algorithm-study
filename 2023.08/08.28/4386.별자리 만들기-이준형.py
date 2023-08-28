from sys import stdin
input = stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]

dists = []

for i in range(n-1):
    for j in range(i+1, n):
        dists.append((((stars[i][0]-stars[j][0])**2+(stars[i][1]-stars[j][1])**2)**0.5, i, j))

dists.sort()
ans, parent = 0, [i for i in range(n)]

for d, a, b in dists:
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        ans += d

print(f"{ans:.2f}")