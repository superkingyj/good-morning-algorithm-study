import sys
sys.setrecursionlimit(100000)
 

T = int(input())

def dfs(x,y):
    gragh[x][y] = '.'
    rows = [-1, 1, 0, 0]
    cols = [0, 0, -1, 1]
    for i in range(4):
        row = rows[i]+x
        col = cols[i]+y
        if 0 <= row < H and 0 <= col < W:
            if gragh[row][col] == '#':
                dfs(row, col)

for _ in range(T):
    H, W = map(int, input().split())
    gragh = [list(sys.stdin.readline()) for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if gragh[i][j] == '#':
                dfs(i, j)
                count += 1
    print(count)      
        