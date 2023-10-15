import sys
sys.setrecursionlimit(10 ** 6)

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

parents = list(range(N))
plan = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            union(i, j)

result = "YES"
for i in range(1, M):
    if parents[plan[i] - 1] != parents[plan[0] - 1]:
        result = "NO"
        break
    
print(result)


