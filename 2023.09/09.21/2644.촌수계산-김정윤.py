import sys

n = int(sys.stdin.readline())

사람1, 사람2 = map(int, sys.stdin.readline().split())
result = 0
m = int(sys.stdin.readline())

arr = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)
    
def dfs(v, num):
    global result
    num += 1
    visited[v] = True
    
    if v == 사람2:
        result = num
    
    for i in arr[v]:
        if not visited[i]:
            dfs(i, num)
            

dfs(사람1, 0)
print(result - 1)