# https://www.acmicpc.net/problem/11279

import sys
import heapq

input = sys.stdin.readline

n = int(input())
max_heapq = []

for _ in range(n) :
    number = int(input())

    if number != 0 :
        heapq.heappush(max_heapq, (-number, number))
    else :
        if not max_heapq :
            print(0)
        else :
            print(heapq.heappop(max_heapq)[1])


