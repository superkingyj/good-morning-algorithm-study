import sys
import math
import heapq

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
ps = []
for i in range(n):
    x, y = map(float, input().split())
    ps.append((x, y))

memo = [[0 for _ in range(n)] for _ in range(n)]

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