import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
K = int(input())

res = 0
for i in range(N):
    zero_cnt = arr[i].count('0')
    if zero_cnt <= K and zero_cnt % 2 == K % 2:
        cnt = 0
        for k in range(N):
            if arr[i] == arr[k]:
                cnt += 1
        res = max(res, cnt)

print(res)