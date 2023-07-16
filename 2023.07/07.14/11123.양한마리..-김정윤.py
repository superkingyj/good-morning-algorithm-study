import sys
# 백준의 재귀 제한 설정
sys.setrecursionlimit(10 ** 6)

def dfs(y, x):
    # #인 것을 체크헀으면, .으로 변경
    arr[y][x] ='.'
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        # 그리드의 높이와 너비를 생각해서 제한
        if ny >= 0 and nx >= 0 and ny < H and nx < W:
            if arr[ny][nx] == '#':
                dfs(ny, nx)

T = int(sys.stdin.readline().rstrip())

# 좌우 설정
dx = [1, 0, -1, 0]
# 상하 설정
dy = [0, 1, 0, -1]



for i in range(T):
    H, W = map(int, sys.stdin.readline().split())
    arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(H)]
    cnt = 0
    for j in range(H):
        for k in range(W):
            if arr[j][k] == '#':
                # 양이면 dfs 함수를 호출, dfs함수는 재귀적으로 근처의 양까지 다 체크한 후 종료 
                dfs(j, k)
                # 그 다음 cnt 1증가
                cnt += 1
    print(cnt)
