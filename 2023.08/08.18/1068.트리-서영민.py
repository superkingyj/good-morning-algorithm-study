import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

tree_list = list(map(int, input().split()))

tree = [[] for _ in range(N+1)]

for node in tree_list:
    tree[node+1].append(node+2)

except_node = int(input())

print(tree)

def bfs():
    q = deque([tree[0]])
    count = 0
    
    while q:
        nodes = q.popleft()
        for node in nodes:
            if node-1 != except_node:
                if not tree[node]:
                    count += 1 
                else:
                    q.append(tree[node])
    
    print(count)
    
bfs()