from sys import stdin
input = stdin.readline

n,m = map(int, input().split())
lamp = [input() for _ in range(n)]
k = int(input())
res = 0

for i in range(n):
    zero = lamp[i].count('0')
    tmp = 0
    if zero<=k and zero%2== k%2:
        for j in range(n):
            if lamp[i] == lamp[j]:
                tmp +=1
    res = max(res, tmp)

print(res)