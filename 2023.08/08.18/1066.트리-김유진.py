import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

def dfs(node):
    tree[node] = -2
    for i in range(N):
        if node == tree[i]:
            dfs(i)

dfs(target)
leaf_cnt = 0

for i in range(N):
    # 지워질 노드라면
    if tree[i] == -2: continue
    # 리프노드가 아니라면
    if i in tree: continue
    leaf_cnt += 1

print(leaf_cnt)