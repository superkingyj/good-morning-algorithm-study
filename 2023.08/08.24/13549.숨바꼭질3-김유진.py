import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [-1] * 100001

def in_range(pos):
    return 0 <= pos < 100001

def can_go(pos):
    if not in_range(pos): return False
    if visited[pos] != -1 : return False
    return True

def bfs():
    q = deque()
    visited[N] = 0
    q.append(N)
    
    while q:
        pos = q.popleft()
        
        if pos == K:
            return visited[pos]
        
        new_pos = pos * 2
        if can_go(new_pos): 
            visited[new_pos] = visited[pos]
            q.append(new_pos)
        
        new_pos = pos -1
        if can_go(new_pos): 
            visited[new_pos] = visited[pos]+1 
            q.append(new_pos)
        
        new_pos = pos + 1
        if can_go(new_pos): 
            visited[new_pos] = visited[pos]+1
            q.append(new_pos)
    
print(bfs())