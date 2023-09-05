import sys
import math
import heapq

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

#별의 갯수
n = int(input())
#별 사이 거리를 저장할 리스트
ps = []

#별 좌표정보
memo = [[0 for _ in range(n)] for _ in range(n)]

#별 사이 거리를 입력받음
for i in range(n):
    x, y = map(float, input().split())
    ps.append((x, y))

#별 사이의 거리를 계산해서 저장
for i in range(n):
    for j in range(n):
        memo[i][j] = math.sqrt((ps[i][0] - ps[j][0]) ** 2 + (ps[i][1] - ps[j][1]) ** 2)

sum = 0
visit = set()
mh = []
heapq.heappush(mh, (0, 0))

while len(visit) <= n - 1:
    cost, cur = heapq.heappop(mh)
    if cur in visit:
        continue
    visit.add(cur)
    sum += cost
    for to in range(n):
        if cur != to and to not in visit:
            heapq.heappush(mh, (memo[cur][to], to))

print(f"{sum:.2f}")