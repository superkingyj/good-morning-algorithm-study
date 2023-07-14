import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
#재귀적으로 노드 탐색
n = int(input())
tree = [[] for _ in range(n + 1)]

#노드 연결
for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])


