import sys
from collections import deque


_input = sys.stdin.readline()


N, M = map(int, input().split())

before = [list(map(int, _input().split())) for _ in range(N)]
after = [list(map(int, input().split())) for _ in range(N)]


def bfs(x, y):
    q = deque
    q.append()