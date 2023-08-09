import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

list = []
visited = [False] * N
previous = 0

def dfs(dep):
    previous = 0
    # 길이가 M이면 list에서 값을 더해줌 즉, 1,9 가 있으면 1 9 로 출력
    if dep == M:
        print(' '.join(map(str, list)))
        return
    for i in range(N):
        # 겹치지 않고 방문하지 않았다면 실행
        if arr[i] != previous and visited[i] == False:
            list.append(arr[i])
            previous = arr[i]
            visited[i] = True
            dfs(dep + 1)
            list.pop()
            visited[i] = False

dfs(0)