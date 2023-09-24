from sys import stdin
input = stdin.readline

N,K = map(int, input().split())
cats = sorted((map(int, input().split())))

start,end = 0,N-1
res = 0
while start<end:
    w = cats[start]+cats[end]
    if w<=K:
        end -=1
        start +=1
        res +=1
    else:
        end -=1

print(res)