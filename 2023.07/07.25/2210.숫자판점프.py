import sys

grid = list(list(map(int, sys.stdin.readline().split())) for _ in range(5))
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
result = set()

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def dfs(x, y, cnt, nums):
    global result
    
    if cnt >= 6: 
        result.add(nums)
        return
    
    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]
        
        if not in_range(new_x, new_y): 
            continue
        
        dfs(new_x, new_y, cnt+1, nums+str(grid[new_x][new_y]))

for i in range(5):
    for j in range(5):
        dfs(i, j, 0, "")

# print(result)
print(len(result))