import sys

def possible(num, broken):
    if num == 0:
        if 0 in broken:
            return 0
        else:
            return 1

    cnt = 0
    while num > 0:
        if num % 10 in broken:
            return 0
        cnt += 1
        num //= 10
    return cnt

target = int(sys.stdin.readline())
n = int(sys.stdin.readline())

broken = set(map(int, sys.stdin.readline().split()))

result = abs(target - 100)

for channel in range(1000001):
    press = possible(channel, broken)
    if press > 0:
        result = min(result, press + abs(target - channel))

print(result)