from sys import stdin
input = stdin.readline
N,M,R=map(int,input().split())
arr=[list(map(int,input().split()))for _ in range(N)]

for k in range(R):
    for j in range(min(N,M)//2):
        x,y=j,j
        pre=arr[x][y]
        #좌
        for i in range(x+1,N-j):
            tmp=arr[i][j]
            arr[i][j]=pre
            pre=tmp
        #하
        for i in range(y+1,M-j):
            tmp=arr[N-1-j][i]
            arr[N-1-j][i]=pre
            pre=tmp
        #우
        for i in range(N-j-2,j-1,-1):
            tmp=arr[i][M-1-j]
            arr[i][M-1-j]=pre
            pre=tmp
        #상
        for i in range(M-2-j,j-1,-1):
            tmp=arr[j][i]
            arr[j][i]=pre
            pre=tmp

for i in arr:
    print(*i)
    
    
# 내가 쓴 코드 아님(속도 테스트용)

# import sys
# input = sys.stdin.readline

# def rotate(A, l, r, t, b, n):
#     while n > 0 and l < r and t < b:
#         indices = [(t, j) for j in range(l, r)]
#         indices += [(i, r) for i in range(t, b)]
#         indices += [(b, j) for j in range(r, l, -1)]
#         indices += [(i, l) for i in range(b, t, -1)]
#         rotated = []
#         for k in range(len(indices)):
#             i, j = indices[(k + n) % len(indices)]
#             rotated.append(A[i][j])
#         for (i, j), v in zip(indices, rotated):
#             A[i][j] = v
#         l, r, t, b = l + 1, r - 1, t + 1, b - 1

# N, M, R = map(int, input().split())
# A = [input().split() for _ in range(N)]
# rotate(A, 0, M - 1, 0, N - 1, R)
# for i, row in enumerate(A):
#     print(' '.join(row))