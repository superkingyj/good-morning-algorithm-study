import sys

input = sys.stdin.readline

N = int(input())

tree_list = list(map(int, input().split()))

delete_node = int(input())


def dfs(node):
    tree_list[node] = -2
    
    for i in range(N):
        if node == tree_list[i]:
            dfs(i)

count = 0

dfs(delete_node)
      
for i in range(N):
    if tree_list[i] != -2 and i not in tree_list:
        count += 1

print(count)