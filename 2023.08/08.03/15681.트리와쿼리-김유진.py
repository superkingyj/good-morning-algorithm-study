import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)


N, R, Q = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
DP = [0] * (N+1)

for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].append(V)
    graph[V].append(U)

def dfs(v):
    DP[v] = 1
    for _v in graph[v]:
        if not DP[_v]:
            dfs(_v)
            DP[v] += DP[_v]

dfs(R)
for _ in range(Q):
    q = int(sys.stdin.readline())
    print(DP[q])