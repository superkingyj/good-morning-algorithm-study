import sys, heapq


N = int(sys.stdin.readline())
hq = []
max_s = 0

for _ in range(N):
    t, s = map(int, sys.stdin.readline().split())
    max_s = max(max_s, s)
    heapq.heappush(hq, (-s, t))

curr_t = max_s
result = 0

while hq:
    s, t= heapq.heappop(hq)
    s = -s
    
    if curr_t < 0:
        result = -1
        break
    else:
        if s < curr_t:
            curr_t = s
        curr_t -= t
        result = curr_t

print(result if curr_t >= 0 else -1)
