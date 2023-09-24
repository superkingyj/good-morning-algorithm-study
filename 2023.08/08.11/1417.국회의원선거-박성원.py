# https://www.acmicpc.net/problem/1417
# 이분탐색? dp? 그리드?

import sys
input = sys.stdin.readline

n = int(input())
me = int(input())

people = [int(input()) for _ in range(n-1)]
people.sort(reverse=True)

count = 0

if n <= 1:
    print(0)
else :
    while me <= people[0] :
        me += 1
        people[0] -= 1
        count += 1
        people.sort(reverse=True)
    print(count)
