import sys

N, M  = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
visited = [False] * N
arr.sort()

def dfs(cnt, permu):
    
    if cnt == M:
        print(" ".join(map(str, permu)))
        return
    
    prev = 0
    for i in range(N):
        if not visited[i] and arr[i] != prev:
            visited[i] = True
            prev = arr[i]
            dfs(cnt+1, permu + [arr[i]])
            visited[i] = False

dfs(0, [])