import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
times.sort()

wait_time = times[0]
total = times[0]

for time in times[1:]:
    wait_time += time
    total += wait_time

print(total)