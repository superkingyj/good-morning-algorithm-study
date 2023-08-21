import sys
from collections import deque

N, S, D, F, B, K = map(int, sys.stdin.readline().split())
police = list(map(int, sys.stdin.readline().split()))
arr = [0] * (N + 1)

# 경찰서 1로 변경
for i in range(K):
    arr[police[i]] = 1


def check(cnt, x):
    queue = deque()
    queue.append((cnt, x))
    
    while queue:
        cnt, x = queue.popleft()
        dx = [x - B, x + F]
        for nx in dx:
            # 넘어가거나 0이전은 continue
            if nx > N or nx < 0:
                continue
            # 경찰서 및 방문했으면 continue
            if arr[nx] == 1:
                continue
            # 집에 도착했다면 +1로 return
            if nx == D:
                return cnt + 1
            arr[nx] = 1
            queue.append((cnt + 1, nx))
            
    return "BUG FOUND"
            
cnt = 0

print(check(cnt, S))
        