import sys
from collections import deque

N, S, D, F, B, K = map(int, sys.stdin.readline().split())
check = [0] * (N+1)

for police_off in list(map(int, sys.stdin.readline().split())):
    check[police_off] = 2

def in_range(pos):
    return 1 <= pos <= N

def can_go(pos):
    if not in_range(pos): return False
    # pos가 방문했거나 경찰서라면
    if check[pos] != 0: return False
    return True


def bfs():
    q = deque()

    check[S] = 1
    q.append((S, 0))
    result = -1
    
    while q:
        pos, cnt = q.popleft()
        
        # 집에 도착했다면 종료
        if pos == D:
            result = cnt
            break
        
        # 앞
        new_pos = pos + F
        if can_go(new_pos):
            check[new_pos] = 1
            q.append((new_pos, cnt+1))
        
        # 뒤
        new_pos = pos - B
        if can_go(new_pos):
            check[new_pos] = 1
            q.append((new_pos, cnt+1))
    
    return "BUG FOUND" if result == -1 else result

print(bfs())
