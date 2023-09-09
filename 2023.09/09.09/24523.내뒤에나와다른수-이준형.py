from sys import stdin
input = stdin.readline

N=int(input())
A=list(map(int,input().split()))
res=[-1]*N
for i in range(N-2,-1,-1):
    if A[i]==A[i+1]:
        res[i]=res[i+1]
    else:
        res[i]=i+2
print(*res)