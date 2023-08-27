from sys import stdin

input = stdin.readline

n = int(input())

li = list(map(int, input().split()))
li.sort()
res = 0
for i in range(n):
    res += li[i] * (2*i-n+1)

print(res*2)
