from sys import stdin

input = stdin.readline
n = int(input())

camp = []
for i in range(n):
    t, s = map(int, input().split())
    camp.append((t, s))

camp = sorted(camp,key= lambda x : -x[1])

res = camp[0][1]-camp[0][0]
for i in range(1,n):
    if res > camp[i][1]:
        res = camp[i][1]-camp[i][0]
    else:
        res -= camp[i][0]

print(res if res >=0 else -1)