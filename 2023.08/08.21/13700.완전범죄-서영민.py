from collections import deque
import sys

input = sys.stdin.readline


N, S, D, F, B, K = map(int, input().split())

visited = [0 for _ in range(N+1)]

if K > 0:
    p_station = list(map(int, input().split()))
    for p in p_station:
        visited[p] = 1


def bfs(s):
    q = deque([(s, 0)])
    
    result = False
    while q:
        
        current_location, count = q.popleft()
        
        visited[current_location] = 1
        
        if current_location == D:
            result = count
            break
        
        front_move = current_location+F
        back_move = current_location-B
        
        if front_move <= N and front_move not in p_station and not visited[front_move]:
            q.append((front_move, count+1))
        
        if back_move > 0 and back_move not in p_station and not visited[back_move]:
            q.append((back_move, count+1))
    
    if result:
        print(result)
    else:
        print("BUG FOUND")
        
bfs(S)