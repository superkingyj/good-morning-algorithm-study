# https://www.acmicpc.net/problem/15903


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

for _ in range(m) :
    li.sort()
    temp = li[0] + li[1]
    li[0] = temp
    li[1] = temp

print(sum(li))