from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

section = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    section.append(list(input()))

visited = [[0]*N for _ in range(N)]

def dfs(x, y, target):
    visited[x][y] = 1
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if section[nx][ny] == target:
                dfs(nx, ny, target)

count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, section[i][j])
            count += 1

print(count, end = ' ')

for i in range(N):
    for j in range(N):
        if section[i][j] == 'G':
            section[i][j] = 'R'

visited = [[0]*N for _ in range(N)]

count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, section[i][j])
            count += 1

print(count)