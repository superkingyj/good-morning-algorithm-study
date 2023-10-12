import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    is_connect = list(map(int, input().split()))
    for k in is_connect:
        if k == 1:
            graph[i].append(k+1)

plan = list(map(int, input().split()))

start = plan[0]

flag = True
for end in plan[1:]:
    if end not in graph[start]:
        flag = False
        break
    start = end

if not flag and M > N:
    print("NO")
else:
    print("YES")