import sys
input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]

arr.sort()

cnt = 1
total = 0

for i in arr:
    total += abs(cnt - i)
    cnt += 1

print(total)