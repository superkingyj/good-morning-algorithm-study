import sys

N, W = map(int, sys.stdin.readline().split())
tree = [0] * (N+1)

for i in range(N-1):
    v1, v2 = map(int, sys.stdin.readline().split())
    
    if tree[v1] < 2:
        tree[v1] += 1
        
    if tree[v2] < 2:
        tree[v2] += 1
        
leaf_cnt = 0
for i in range(2, N+1):
    if tree[i] == 1: 
        leaf_cnt += 1
        
print(W / leaf_cnt)