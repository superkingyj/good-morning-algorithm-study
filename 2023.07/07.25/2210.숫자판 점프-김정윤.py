import sys
sys.setrecursionlimit(10 ** 6)

arr = []
result = set()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, l):
    l += arr[x][y]
    
    if len(l) == 6:
        result.add(l)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
            dfs(nx, ny, l)


for i in range(5):
    arr.append(list(map(str, sys.stdin.readline().split())))
    
for i in range(5):
    for j in range(5):
        dfs(i, j, "")
        
print(len(result))