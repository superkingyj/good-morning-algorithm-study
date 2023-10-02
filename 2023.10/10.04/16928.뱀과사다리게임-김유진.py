import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
ladder = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(N))
snake = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(M))
visited = [False] * (101)

def in_range(x):
    return 1 <= x <= 100

def can_go(x):
    if not in_range(x): return False
    if visited[x]: return False
    return True

def bfs():
    q = deque()
    q.append((1, 0))
    visited[1] = True
    result = sys.maxsize
    
    while q:
        x, cnt = q.popleft()
        
        if x == 100:
            result = cnt
            break 
        
        for i in range(1, 7):
            new_x = x + i
            
            for start, end in ladder:
                if new_x == start: new_x = end
            for start, end in snake:
                if new_x == start: new_x = end
            
            if can_go(new_x):
                visited[new_x] = True
                q.append((new_x, cnt+1))

    return result

print(bfs())