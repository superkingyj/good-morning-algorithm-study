# https://www.acmicpc.net/problem/4158

import sys
input = sys.stdin.readline

while True :
    n, m = map(int, input().split())
    if n == 0 and m == 0 :
        break
    cd_dict = {}
    count = 0

    for _ in range(n) :
        cd = int(input())
        cd_dict[cd] = 1
    
    for _ in range(m) :
        cd = int(input())
        if cd in cd_dict :
            count += 1

    print(count)




# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# sy = [int(input()) for _ in range(n)]
# sk = [int(input()) for _ in range(m)]
# a, b = map(int, input().split())

# count = 0
# for cd in sk :
#     if cd in sy :
#         count += 1

# print(count)




