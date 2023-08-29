N = int(input())

schedule = [tuple(map(int, input().split())) for _ in range(N)]

schedule.sort(key=lambda x :x[1], reverse=True)

time, limit = schedule[0][0], schedule[0][1]

start = limit - time

for i in range(1, len(schedule)):
    time, limit = schedule[i][0], schedule[i][1]
    if start > limit:
        start = limit - time
    else:
        start -= schedule[i][0]

if start >= 0:
    print(start)
else:
    print(-1)

    