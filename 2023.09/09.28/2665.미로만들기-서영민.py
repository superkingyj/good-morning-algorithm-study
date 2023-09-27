import heapq
import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().strip())) for _ in range(N)]

def bfs():
    heap = []
    heap.append((0,0,0))
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    arr[0][0] = -1
    while heap:
        count, x, y = heapq.heappop(heap)
        
        if x == N - 1 and y == N - 1:
            print(count)
            break
        
        for a, b in zip(dx, dy):
            nx, ny = x+a, y+b
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != -1:
                if arr[nx][ny] == 1:
                    temp = count
                else:
                    temp = count + 1
                arr[nx][ny] = -1
                heapq.heappush(heap, (temp, nx, ny))
    
bfs()