import math

N = int(input())

dots = [list(map(float, input().split())) for _ in range(N)]

def distance(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    return math.sqrt((x1-x2)**2+ (y1-y2)**2) 

lengths = []
for i in range(N):
    for k in range(i+1, N):
        lengths.append(distance(dots[i], dots[k]), i, k)
        
lengths.sort()

