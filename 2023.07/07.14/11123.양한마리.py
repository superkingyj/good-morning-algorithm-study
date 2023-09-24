# import sys
# input = sys.stdin.readline

# T = int(input())

# # dfs 를 먼저 구성


def dfs(graph, visited, row, col):
    visited[row][col] = True

    dr = [-1, 1, 0, 0]  # 인접한 격자로만 이동 (상하좌우)
    dc = [0, 0, -1, 1]  # 인접한 격자로만 이동 (상하좌우)
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]) and not visited[nr][nc] and graph[nr][nc] == '#':
            dfs(graph, visited, nr, nc)


T = int(input())  # 테스트 케이스 개수 입력
for _ in range(T):
    H, W = map(int, input().split())  # 그래프의 높이와 너비 입력

###.    graph = []  # 그래프 정보를 저장할 리스트
    visited = [[False] * W for _ in range(H)]  # 방문 여부를 저장할 2차원 리스트

    for _ in range(H):
    
        graph.append(input())  # 그래프 정보 입력

    count = 0  # 양이 있는 덩어리의 개수를 저장할 변수

    for i in range(H):
        for j in range(W):
            if not visited[i][j] and graph[i][j] == '#':
                count += 1
                dfs(graph, visited, i, j)

    print(count)  # 양이 있는 덩어리의 개수 출력

# 이 문제는 어떤 문제이고
# 나는 이렇게 문제를 접근했고
# 이 문제를 위해 어떻게 풀었고
# 시간복잡도는 이렇다