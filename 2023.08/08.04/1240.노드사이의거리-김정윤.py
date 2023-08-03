import sys
sys.setrecursionlimit (10 ** 6)

N, M = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(N + 1)]


def finddistance(n1, n2):
    visited[n1] = 1
    for i in tree[n1]:
        EndNode, dist = i
        if not visited[EndNode]:
            if EndNode == n2:
                return dist
            d = finddistance(EndNode, n2)
            if d != -1:
                return dist + d
    return -1
            
            
        


for i in range(N - 1):
    startNode, EndNode, distance = map(int, sys.stdin.readline().split())
    tree[startNode].append((EndNode, distance))
    tree[EndNode].append((startNode, distance))
    

for i in range(M):
    visited = [0] * (N + 1)
    start, end = map(int, sys.stdin.readline().split())
    result = finddistance(start, end)
    print(result)