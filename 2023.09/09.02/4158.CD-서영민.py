import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    
    if N == 0 and M == 0:
        break
    
    A = set(int(input()) for _ in range(N))
    B = set(int(input()) for _ in range(M))
    
    cnt = A.intersection(B)
    print(len(cnt))
     