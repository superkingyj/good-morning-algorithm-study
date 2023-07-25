import sys
from itertools import product

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

num = list(list(map(int, input().split())) for _ in range(5))
result = []

for i in range(5):
    for j in range(5):
        for dir in product(range(4), repeat=5):        
            temp = []
            temp.append(num[i][j])
            x, y = i, j
            for k in dir:
                x, y = x + dx[k], y + dy[k]
                if not (0 <= x < 5 and 0 <= y < 5):     
                    break
                temp.append(num[x][y])
            if len(temp) == 6:
                result.append("".join(map(str, temp)))  

print(len(set(result))) 