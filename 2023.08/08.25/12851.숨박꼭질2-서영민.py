from collections import deque

N,K = map(int,input().split())
q= deque()
q.append(N)
visited = [-1] * 100001
visited[N]=0

count = 0
while q:
    now = q.popleft()
    if now == K:
        time = visited[now]
        count += 1
        continue
    
    for i in [now-1, now*2, now+1]:
        if 0 <= i < 100001 and (visited[i] == -1 or visited[i] == visited[now] + 1):
            visited[i] = visited[now] + 1 
            q.append(i)   
    
print(time, count, sep='\n')