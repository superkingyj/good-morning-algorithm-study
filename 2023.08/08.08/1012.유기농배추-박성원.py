# https://www.acmicpc.net/problem/1012
# 브루트포스 및 달팽이 문제

import sys
input = sys.stdin.readline

T = int(input())
m, n, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

x = [0, 0, 1, -1]
y = [1, -1, 0, 0]

for i in range(k) :
    row, col = map(int, input().split())
    graph[col][row] = 1

print(graph)
