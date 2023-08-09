# https://www.acmicpc.net/problem/2512

import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
target = int(input())

start, end = 0, max(li)

while start <= end :
    mid = (start+end) // 2
    budgets = 0

    for money in li :
        if money > mid :
            budgets += mid
        else :
            budgets += money


    if budgets <= target :
        start = mid + 1
    else :
        end = mid - 1

print(end)