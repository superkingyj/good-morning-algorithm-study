import sys
import heapq
N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, -1 * x)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))