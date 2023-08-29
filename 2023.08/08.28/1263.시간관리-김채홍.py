import sys

input = sys.stdin.readline

N = int(input())
work = []

for _ in range(N):
    t, s = map(int, input().split())
    work.append((t, s))

work.sort(key=lambda x: (x[1], x[0]), reverse=True)

time = work[0][1]
for i in range(1, N):
    if time < work[i][1]:
        time -= work[i][0]
    else:
        time = work[i][1] - work[i][0]

if time < 0:
    print(-1)
else:
    print(time)