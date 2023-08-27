# https://www.acmicpc.net/problem/12851

from collections import deque

n, k = map(int, input().split())
queue = deque()
queue.append(n)
visited = [-1] * 100001
visited[n] = 0

result = 0
count = 0

while queue :
    s = queue.popleft()
    temp = visited[s]
    if s == k :
        result = temp
        count += 1
        continue

    for i in [s-1, s+1, s*2] :
        if 0 <= i < 100001 and (visited[i] == -1 or visited[i] == visited[s] + 1) :
            visited[i] = visited[s] + 1
            queue.append(i)

print(result)
print(count)
        

