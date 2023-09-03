import sys
from collections import defaultdict

N = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(N):
    n, l, r = sys.stdin.readline().strip().split()
    graph[n].append(l)
    graph[n].append(r)


def preorder(node):
    if node != ".":
        print(node, end="")
        preorder(graph[node][0])
        preorder(graph[node][1])


def inorder(node):
    if node != ".":
        inorder(graph[node][0])
        print(node, end="")
        inorder(graph[node][1])


def postorder(node):
    if node != ".":
        postorder(graph[node][0])
        postorder(graph[node][1])
        print(node, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
