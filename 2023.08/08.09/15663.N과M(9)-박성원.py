# https://www.acmicpc.net/problem/15663

# dfs? queue? 브루트포스?
# dfs로 본이유 : 중복되는 수열을 여러번 출력하면 안되며 에서 방문여부를 확인하는 요소때문에 dfs로 봄

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))

visited = [False] * n
temp = []

def dfs():
    if len(temp) == m :
        print(*temp)
        return
    remember = 0
    for i in range(n) :
        if not visited[i] and remember != li[i] :
            visited[i] = True
            temp.append(li[i])
            remember = li[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()