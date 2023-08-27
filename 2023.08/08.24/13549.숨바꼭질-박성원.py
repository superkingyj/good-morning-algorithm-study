# https://www.acmicpc.net/problem/13549

# x-1 or x+1 ? bfs인가 싶다.

from collections import deque

n, k = map(int, input().split())
queue = deque()

# 처음위치 추가
queue.append(n)

# 방문여부 초기화
visited = [-1 for _ in range(100001)]
visited[n] = 0


while queue :
    s = queue.popleft()
    if s == k :
        print(visited[s])
        break
    if 0 <= s-1 < 100001 and visited[s-1] == -1 :
        visited[s-1] = visited[s] + 1
        queue.append(s-1)
    if 0 < s*2 < 100001 and visited[s*2] == -1 :
        visited[s*2] = visited[s]
        queue.appendleft(s*2) # s*2 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    if 0 <= s+1 < 100001 and visited[s+1] == -1 :
        visited[s+1] = visited[s] + 1
        queue.append(s+1)
        

