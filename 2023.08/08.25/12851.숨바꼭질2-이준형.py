from collections import deque

N,K = map(int ,input().split())
queue = deque()
queue.append(N)
visited = [0]*100001
cnt, res = 0,0

while queue:
    x = queue.popleft()
    tmp = visited[x]
    if x == K:
        res = tmp
        cnt +=1
        continue
    
    for i in [x-1,x+1,x*2]:
        if 0<=i<100001 and (not visited[i] or visited[i] == tmp+1):
            queue.append(i)
            visited[i] = tmp+1

print(res)
print(cnt)