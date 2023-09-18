# import sys

# Q = int(sys.stdin.readline())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 우, 하, 좌, 상

def in_range(n, x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, n, visited):
    if not in_range(n, x, y): return False
    if visited[x][y]: return False
    return True

def make_snail_array(n, tar_x=-1, tar_y=-1, z=-1):
    print("만드는 중")
    
    visited = [[False] * n for _ in range(n)]
    snail_array = [[-1] * n for _ in range(n)]
    dir, x, y = 0, 0, 0
    z_x, z_y = -1, -1
    
    for num in range(1, n*n+1):
        visited[x][y] = True
        snail_array[x][y] = num
        # if num == z: 
        #     z_x, z_y = x+1, y+1
        #     return (z_x, z_y)

        # if x == tar_x and y == tar_y:
        #     return num
        
        new_x, new_y = x + dx[dir], y + dy[dir]
        if not can_go(new_x, new_y, n, visited):
            dir = (dir + 1) % 4
            new_x, new_y = x + dx[dir], y + dy[dir]
        
        x, y = new_x, new_y
    
    return snail_array
    
f = open("snail_array.txt", 'w')
snail_array = make_snail_array(9999)
for i in range(9999):
    f.writelines(str(snail_array[i]) + '\n')
f.close()

# for _ in range(Q):
#     input = list(map(int, sys.stdin.readline().split()))
    
#     # 크기가 n인 이차원 달팽이 배열에서 x행 y열에 있는 수 출력
#     if input[0] == 1:
#         n, x, y = input[1:]
#         print(make_snail_array(n=n, tar_x=x-1, tar_y=y-1))
        
#     # 크기가 n인 이차원 달팽이 배열에서 z가 들어있는 행 번호와 열 번호를 공백으로 구분해 출력
#     else:
#         n, z = input[1:]
#         print(*make_snail_array(n=n, z=z))