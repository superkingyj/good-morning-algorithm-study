import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        if x < 0:
            heapq.heappush(heap, ((-1 * x), -1))
        else:
            heapq.heappush(heap, (x, 1))
    else:
        if len(heap) == 0:
            print(0)
        else:
            k, m = heapq.heappop(heap)
            print(k * m)