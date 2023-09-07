# https://www.acmicpc.net/problem/15661

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

li = []

for i in range(n) :
    for j in range(0, i) :
        li.append(board[i][j] + board[j][i])

min_num = 1e9

for k in range(n) :
    for l in range(k, n) :
        temp = abs(li[k] - li[l])
        min_num = min(min_num, temp)

print(min_num)