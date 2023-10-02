from sys import stdin
import heapq

input = stdin.readline
heap = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num:
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)