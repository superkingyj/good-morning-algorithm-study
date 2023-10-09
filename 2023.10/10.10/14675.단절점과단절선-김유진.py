import sys
from collections import defaultdict

N = int(sys.stdin.readline())
tree = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(sys.stdin.readline())

for _ in range(q):
    t, k = map(int, sys.stdin.readline().split())
    # 단절점인지 질의
    if t == 1:
        # 리프노드라면
        if len(tree[k]) < 2:
            print("no")
        else:
            print("yes")
    # 단절선인지 질의
    else:
        print("yes")


"""
트리에서 단절점이 아닌 노드
1. 리프노드
2. 자식이 하나인 루트노드

트리에서 단절선이 아닌경우
=> 트리는 사이클이 없으므로 모든 간선이 단절점임
"""
