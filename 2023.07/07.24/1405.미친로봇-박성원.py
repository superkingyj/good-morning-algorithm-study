import sys
input = sys.stdin.readline

n, E,W,S,N = map(int, input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]
compass = [E,W,S,N]

graph = [[0] * (2*n+1) for _ in range(2*n+1)]

answer = 0
def dfs(x,y,percent,cnt) :
    global answer
    if cnt == n:
        answer += percent
        return
    now_percent = percent
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < (2*n+1) and 0 <= ny < (2*n+1) :
            if graph[nx][ny] == 1 :
                continue
            else :
                dfs(nx, ny, now_percent*(compass[i]/100), cnt+1)
                graph[nx][ny] = 0

dfs(n,n,1,0)

print(answer)



