# https://www.acmicpc.net/problem/1263

# 문제이해가 한번 필요함

import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li.sort(key = lambda x : x[1], reverse=True)



# 왜 li[0][1] - li[0][0] 을 왜 하는것인가?
result = li[0][1] - li[0][0]

for i in range(1, n) :
    if result > li[i][1] :
        result = li[i][1] - li[i][0]
    else :
        result -= li[i][0]

print(result if result >= 0 else -1)
