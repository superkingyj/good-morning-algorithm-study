from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def checkDownCnt(fallLst, check):
    downCnt, flag = 1, 0
    while True:
        for r, c in fallLst:
            if r+downCnt == R-1:
                flag = 1
                break
            if cave[r+downCnt+1][c] == 'x' and check[r+downCnt+1][c]:
                flag = 1
                break
        if flag:
            break
        downCnt += 1
    return downCnt

def checkLand():
    check = [[0] * C for _ in range(R)]
    for lc in range(C):
        if cave[R-1][lc] == "x" and not check[R-1][lc]:
            check[R-1][lc] = 1
            Q = deque([(R-1, lc)])
            while Q:
                r, c = Q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if cave[nr][nc] == "x" and not check[nr][nc]:
                        check[nr][nc] = 1
                        Q.append((nr, nc))
    return check


def breakMinerals(br, bc):

    check = checkLand()

    minerals = []
    fallLst = []
    for nd in range(4):
        r = br + dr[nd]
        c = bc + dc[nd]
        if not (0 <= r < R and 0 <= c < C):
            continue

        if cave[r][c] == "x" and not check[r][c]:
            Q = deque([(r, c)])
            check[r][c] = 2
            minerals.append((r, c))
            cave[r][c] = "."
            while Q:
                r, c = Q.popleft()
                if cave[r+1][c] == ".":
                    fallLst.append((r, c))
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if cave[nr][nc] == "x" and not check[nr][nc]:
                        check[nr][nc] = 2
                        Q.append((nr, nc))
                        minerals.append((nr, nc))
                        cave[nr][nc] = "."

    if fallLst: 
        downCnt = checkDownCnt(fallLst, check)
        for mr, mc in minerals:
            cave[mr+downCnt][mc] = "x"


R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))

for i in range(N):
    br = R - heights[i]
    if not i % 2:
        for bc in range(C):
            if cave[br][bc] == "x":
                cave[br][bc] = "."
                breakMinerals(br, bc)
                break
    else:
        for bc in range(C-1, -1, -1):
            if cave[br][bc] == "x":
                cave[br][bc] = "."
                breakMinerals(br, bc)
                break
for row in cave:
    print(''.join(row))
    