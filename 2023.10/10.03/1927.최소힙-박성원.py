# https://www.acmicpc.net/problem/1927

import sys
import heapq

input = sys.stdin.readline

n = int(input())
min_heapq = []

for _ in range(n) :
    number = int(input())

    if number != 0 :
        heapq.heappush(min_heapq, number)
    else :
        if not min_heapq :
            print(0)
        else :
            print(heapq.heappop(min_heapq))
