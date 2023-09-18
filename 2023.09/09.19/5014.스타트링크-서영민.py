from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)

def bfs():
    q = deque()
    q.append((S, 0))
    visited[S] = 1
    flag = True
    while q:
        now, count = q.popleft()
        
        if now == G:
            flag = False
            print(count)
            break
        
        if now + U <= F and not visited[now+U] and U > 0:
            visited[now+U] = 1
            q.append((now+U, count + 1))
        if now - D >= 1 and not visited[now-D] and D > 0:
            visited[now-D] = 1
            q.append((now-D, count + 1))
    if flag:
        print('use the stairs')
        
bfs()