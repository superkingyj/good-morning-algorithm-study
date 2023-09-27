# https://www.acmicpc.net/problem/2665

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra() :
    heap = []
    heappush(heap, [0,0,0])
    visited[0][0] = 1

    while heap :
        a, x, y = heappop(heap)

        if x == n -1 and y == n - 1 :
            print(a)
            return
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n  and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                if board[nx][ny] == 0 :
                    heappush(heap, [a+1, nx, ny])
                else :
                    heappush(heap, [a, nx, ny])

dijkstra()
    
    