import heapq
import sys


def dijkstra(start):
    q = [(0, start)]
    times = [float('inf')] * (n + 1)
    times[start] = 0
    while q:
        time, node = heapq.heappop(q)
        for neighbor, nt in graph[node]:
            nt += time
            if times[neighbor] > nt:
                times[neighbor] = nt
                heapq.heappush(q, (nt, neighbor))
    return times


t = int(input())

for _ in range(t):
    n, d, c = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)] 
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a, s))
    times = dijkstra(c)
    count = 0
    result = 0
    for time in times:
        if time != float('inf'):
            count += 1
            result = max(time, result)

    print(count, result)
