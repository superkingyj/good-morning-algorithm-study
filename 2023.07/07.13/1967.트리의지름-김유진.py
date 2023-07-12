import sys
from itertools import combinations
from collections import defaultdict

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = defaultdict(list)
nodes = set()
start_node, start_dist = 0, 0
end_node, end_dist = 0, 0
max_diamter = 0

for _ in range(N-1):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
    
    
def dfs(curr, weight, flag):
    global start_dist, start_node, end_node, end_dist
    
    visited[curr] = True
    
    if flag == "start" and weight > start_dist:
        start_dist = weight
        start_node = curr
        
    if flag == "end" and weight > end_dist:
        end_dist = weight
        end_node = curr
    
    for _node, _weight in graph[curr]:
        if not visited[_node]:
            dfs(_node, weight+_weight, flag)    

# 1번 노드에서부터 가장 먼 곳(start_node) 찾기
visited = [True] + [False] * N
dfs(1, 0, "start")

# start_node에서부터 가장 먼 곳(end_node) 찾기
visited = [True] + [False] * N
dfs(start_node, 0, "end")

print(end_dist)