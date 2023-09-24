# https://www.acmicpc.net/problem/1916

import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
m = int(input())
li = [[] for _ in range(n+1)]
dist = [sys.maxsize] * (n+1)
visit = [False] * (n+1)

for _ in range(m) :
    start, end, weight = map(int, input().split())
    li[start].append((end, weight))

start_index, end_index = map(int, input().split())

def dijkstra(start, end) :
    # 우선순위 큐에 넣고 시작
    pq = PriorityQueue()
    pq.put((0, start))

    dist[start] = 0
    while pq.qsize() > 0 :
        nowNode = pq.get()
        now = nowNode[1]
        if not visit[now] :
            visit[now] = True
            for n in li[now] :
                if not visit[n[0]] and dist[n[0]] > dist[now] + n[1] :
                    dist[n[0]] = dist[now] + n[1]
                    pq.put((dist[n[0]], n[0]))

    return dist[end]

print(dijkstra(start_index, end_index))