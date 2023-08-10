import sys
import heapq

N = int(sys.stdin.readline())
hq = []
dasom = int(sys.stdin.readline())

for _ in range(N-1):
    heapq.heappush(hq, -int(sys.stdin.readline()),)
    

if N == 1:
    print(0)
else:
    cnt = 0
    
    while True:
        max_num = heapq.heappop(hq)
        
        if -max_num < dasom:
            break
        
        heapq.heappush(hq, max_num+1)
        cnt += 1
        dasom += 1
    
    print(cnt)