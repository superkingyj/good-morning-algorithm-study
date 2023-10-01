import sys
import heapq

N = int(sys.stdin.readline())
q = []

for _ in range(N):
    num = int(sys.stdin.readline())
    
    if num == 0:
        if not q: print(0)
        else: 
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, num)