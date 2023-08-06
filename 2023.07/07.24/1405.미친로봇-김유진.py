import sys

N, East, West, South, North = map(int, sys.stdin.readline().split()) 
dx = [1, -1, 0]
dy = [0, 0, 1, -1]
percent_dir = [East, West, South, North]
visited = [[0] * (2*N+1) for _ in range(2*N+1)]
result = 0

def in_range(x,y):
    return 0 <= x < (2*N+1) and 0 <= y < (2*N+1)

def can_go(x,y):
    if not in_range(x,y): return False
    if visited[x][y]: return False
    return True

def dfs(x, y, cnt, percent):
    global result
    
    if cnt == N:
        result += percent
        return
    
    curr_percent = percent
    visited[x][y] = True
    
    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]
        
        if can_go(new_x, new_y):
            
            dfs(new_x, new_y, cnt+1, curr_percent * (percent_dir[i]/100))
            visited[new_x][new_x] = True
            
dfs(N, N, 0, 1)
print(result)