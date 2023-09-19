import sys
input = sys.stdin.readline

def get_n(a):
    N = a
    target = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    arr = [[0] * N for _ in range(N)]
    cnt = 1

    d_idx = 0
    x, y = 0, 0
    for _ in range(N**2):
        if x >= N or x < 0 or y >= N or y < 0 or arr[x][y] != 0:
            
            x -= dx[d_idx]
            y -= dy[d_idx]
            if d_idx >= 3:
                d_idx = 0
            else:
                d_idx += 1
            x += dx[d_idx]
            y += dy[d_idx]
        
        arr[x][y] = cnt
         
        cnt += 1
        x += dx[d_idx]
        y += dy[d_idx]
    return arr


N = int(input())

for _ in range(N):
    data = list(map(int, input().split()))
    if data[0] == 1:
        n, x, y = data[1], data[2], data[3]
        arr = get_n(n)
        print(arr[x-1][y-1])
    elif data[0] == 2:
        n, z = data[1], data[2]
        arr = get_n(n)
        for i in range(n):
            if z in arr[i]:
                print(i+1, arr[i].index(z)+1)