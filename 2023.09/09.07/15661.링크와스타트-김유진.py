import sys

N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = sys.maxsize
visited = [False] *  (N)

def get_diff():
    start = 0
    link = 0
    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:
                start += grid[i][j]
            elif not visited[i] and not visited[j]:
                link += grid[i][j]

    return abs(start - link)


def dfs(idx):
    global result
    
    if idx == N:
        diff = get_diff()
        result = min(result, diff)
        return
    
    visited[idx] = True
    dfs(idx+1)
    visited[idx] = False
    dfs(idx+1)
    
    
dfs(0)
print(result)