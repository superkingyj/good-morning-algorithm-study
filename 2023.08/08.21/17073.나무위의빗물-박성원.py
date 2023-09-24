# https://www.acmicpc.net/problem/17073
# defaultdict 랑 그냥 dict 의 차이?
# 그래프문제 -> bfs

import sys
from collections import deque, defaultdict

input = sys.stdin.readline
tree = defaultdict(list)
n, w = map(int, input().split())

for _ in range(n-1) :
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

leaf_count = 0

for root, nodes in tree.items() :
    if root != 1 and len(nodes) == 1 :
        leaf_count += 1

print(round(w/leaf_count, 10))