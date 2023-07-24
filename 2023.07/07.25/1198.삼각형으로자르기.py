import sys

N = int(sys.stdin.readline())
vertex = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_area = 0

def get_area_of_triangle(x1, y1, x2, y2, x3, y3):
    first = (x1 * y2) + (x2 * y3) + (x3 * y1)
    second = (y1 * x2) + (y2 * x3) + (y3 * x1)
    area = (first - second) * 0.5
    
    if area >= 0: return area
    else: return area * -1 

def dfs(target):
    global max_area
    
    if len(target) == 3:
        x1, y1 = target[0]
        x2, y2 = target[1]
        x3, y3 = target[2]
        area = get_area_of_triangle(x1, y1, x2, y2, x3, y3)
        max_area = max(max_area, area)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            target.append(vertex[i])
            dfs(target)
            target.pop()
            visited[i] = False
 
        
visited = [False] * N
dfs([])
print(max_area)