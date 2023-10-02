import sys
import heapq

N = int(sys.stdin.readline())
hq = []

for _ in range(N):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if hq:
            val, num = heapq.heappop(hq)
            print(num)
        else: print(0)
    else:
        val, num = abs(x), x
        heapq.heappush(hq, (val, num))

        