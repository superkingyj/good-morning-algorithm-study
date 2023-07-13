import sys
sys.setrecursionlimit(1000000000)

def dfs(y, x):
    graph[y][x] = '.'   #지나간 곳 표시
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < H) and (0 <= X < W) and graph[Y][X] == '#':    #좌표에'#' 확인
            dfs(Y, X)


for _ in range(int(input())):           #입력 받을 테스트 케이스 수
    H, W = map(int, input().split())    #높이와 너비를 입력받는다.
    graph = [list(input()) for _ in range(H)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]   #그리드 공간
    count = 0

    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#':  # 양 발견
                dfs(i, j)
                count += 1
    
    print(count)