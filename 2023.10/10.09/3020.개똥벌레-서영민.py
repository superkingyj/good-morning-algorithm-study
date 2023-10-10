import sys
input = sys.stdin.readline
from bisect import bisect_left

N, H = map(int, input().split())


bot = [] 
top = []

for i in range(N):
    length = int(input())
    if i % 2 == 0:
        bot.append(length)
    else:
        top.append(length)
        
top.sort()
bot.sort()

min_res = sys.maxsize
res_cnt = 1

for i in range(H):
    b = bisect_left(bot, i+1)
    t = bisect_left(top, H-i)
    cnt = N - (b+t)
    if min_res > cnt:
        min_res = cnt
        res_cnt = 1
    elif min_res == cnt:
        res_cnt += 1

print(min_res, res_cnt)