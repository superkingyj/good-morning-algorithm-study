import sys
from collections import defaultdict
from collections import deque

T = int(sys.stdin.readline())

def bfs(V1, V2):
    visited = [False] * (N+1)
    visited[V1] = True
    visited[V2] = True
    q = deque()
    q.append(V1)
    q.append(V2)

    while q:
        v = q.pop()
        for _v in tree[v]:
            if visited[_v]:
                return _v
            if not visited[_v]:
                visited[_v] = True
                q.append(_v)


for _ in range(T):
    N = int(sys.stdin.readline())
    tree = defaultdict(list)

    for _ in range(N-1):
        A, B = map(int, sys.stdin.readline().split())
        tree[B].append(A)
    
    V1, V2 = map(int, sys.stdin.readline().split())
    print(bfs(V1, V2))