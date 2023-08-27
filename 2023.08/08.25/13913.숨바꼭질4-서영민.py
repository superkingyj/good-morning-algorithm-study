from collections import deque
from collections import defaultdict

N,K = map(int,input().split())
q= deque()
q.append(N)
visited = [-1] * 100001
location = defaultdict(int)
visited[N]=0

count = 0
while q:
    now = q.popleft()
    if now == K:
        lc_list = []
        time = visited[now]
        temp = now
        count += 1
        while temp != N:
            lc_list.append(temp)
            temp = location[temp]
        lc_list.append(N)
        lc_list.reverse()
        break
    
    for i in [now-1, now*2, now+1]:
        if 0 <= i < 100001 and visited[i] == -1:
            visited[i] = visited[now] + 1 
            location[i] = now
            q.append(i)   
    
print(time)
print(*lc_list)