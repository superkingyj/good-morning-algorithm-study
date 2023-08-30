from sys import stdin
input = stdin.readline

n = int(input())
k = int(input())
li = list(map(int, input().split()))

pic = dict()

for i in range(k):
    if li[i] in pic:
        pic[li[i]] +=1
    else:
        if len(pic)>=n:
            for key, val in pic.items():
                if val == min(pic.values()):
                    del(pic[key])
                    break
        pic[li[i]] = 1

res = sorted(pic.keys())
print(*res, sep=' ')
            