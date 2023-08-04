import sys

_input = sys.stdin.readline

m , n , h = map(int, _input().split())

tomato_boxes = []

for _ in range(h):
    for i in range(m):
        box = [list(map(int, _input().split())) for _ in range(n)]
        tomato_boxes.append(box)
        
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dz = [i for i in range(h)]

def dfs(x, y, z):
      
