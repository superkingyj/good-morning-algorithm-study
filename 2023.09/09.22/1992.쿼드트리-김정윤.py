import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def quad(x, y, n):
    ck = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if ck != arr[i][j]:
                ck = -1
                break
            
    if ck == -1:
        print('(', end='')
        n //= 2
        quad(x, y, n)
        quad(x, y + n, n)
        quad(x + n, y, n)
        quad(x + n, y + n, n)
        print(')', end='')
        
    elif ck == 1:
        print(1, end = '')
    else:
        print(0, end='')

quad(0, 0, N)