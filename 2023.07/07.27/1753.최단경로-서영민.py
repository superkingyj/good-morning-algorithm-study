import sys

_input = sys.stdin.readline

def dijkstra():
    pass

V, E = map(int, _input().split())

graph = [0]*(V+1)

for i in range(1, V+1):
    u ,v, w = map(int, _input().split())
    
