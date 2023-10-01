from sys import stdin
import heapq

input = stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap):
            print(-1*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)