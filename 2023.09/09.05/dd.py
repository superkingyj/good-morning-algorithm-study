import sys
from collections import deque

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
        
        
def bfs(x):
    q = deque()
    q.append(x)
    check = [0] * N
    
    while q:
        temp = q.popleft()
        
        for i in range(N):
            if check[i] == 0 and arr[temp][i] == 1:
                q.append(i)
                check[i] = 1
                visited[x][i] = 1
                
for i in range(N):
    bfs(i)
    
for i in visited:
    print(*i)