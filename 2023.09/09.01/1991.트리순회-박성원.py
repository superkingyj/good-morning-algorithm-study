# https://www.acmicpc.net/problem/1991

import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n) :
    a, b, c = map(str, input().split())
    tree[a] = b,c
# 전위 순회 : 서브트리의 루트를 먼저 확인 후 자식 노드를 확인하는 순회방법
def preorder(root) :
    if root != '.' :
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위 순회 : 왼쪽자식, 루트노드, 오른쪽 자식 노드 순으로 확인
def inorder(root) :
    if root != '.' :
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

# 후위 순휘 : 자식 노드를 모두 확인한 후에 루트도느를 확인하는 순회방법
def postorder(root) :
    if root != '.' :
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')