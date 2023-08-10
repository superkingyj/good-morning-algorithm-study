# https://www.acmicpc.net/problem/15664

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
visited = [False] * n
temp = []

def dfs(start) :
    if len(temp) == m :
        print(*temp)
        return
    
    remember = 0

    for i in range(start, n) :
        if not visited[i] and remember != li[i] :
            visited[i] = True
            temp.append(li[i])
            remember = li[i]
            dfs(i+1)
            visited[i] = False
            temp.pop()

dfs(0)