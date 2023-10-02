import sys
import heapq
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    number = int(input())
    if number == 0 and not heap:
        print(0)
    elif number == 0:
        print(-1 * heapq.heappop(heap))
    else:
        heapq.heappush(heap, -number)