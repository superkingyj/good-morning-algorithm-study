# 시간초과
# import sys
# input = sys.stdin.readline

# n, s = map(int, input().split())
# li = list(map(int, input().split()))

# count = 1e9

# for i in range(len(li)-1) :
#     sum_li = li[i]
#     temp = 0
#     for j in range(i+1, len(li)-1) :
#         if sum_li < s :
#             sum_li += li[j]
#             temp += 1
#         else : 
#             break
#         count = min(count, temp)

# print(count+1)

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
li = list(map(int, input().split()))

left, right = 0,0
sum_li = 0
length = sys.maxsize

while True :
    if sum_li < s :
        length = min(length, right-left)
        sum_li += li[right]
        right += 1
    elif sum_li >= s :
        sum_li -= li[left]
        left += 1
    else :
        break

if length == sys.maxsize :
    print(0)
else :
    pass