import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())

shops = []
for i in range(K+1):
    x, y = map(int, input().split())
    
    if i == K :
        my_x, my_y = x, y
    else:
        shops.append((x, y))
        
res = 0

def calc_dist(dir, dist):
    
    if dir == 1:
        return dist
    elif dir == 2:
        return M + N + (M - dist)
    elif dir == 3:
        return N + M + M + (N - dist)
    else:
        return dist + M
    
my_dist = calc_dist(my_x, my_y)

res = 0
for x, y in shops:
    dist = calc_dist(x, y)
    temp1 = abs(my_dist - dist)
    temp2 = 2 * M + 2 * N - temp1
    res += min(temp1, temp2)

print(res)