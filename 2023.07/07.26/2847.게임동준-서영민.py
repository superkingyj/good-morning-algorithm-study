N = int(input())

scores = [int(input()) for _ in range(N)]


count = 0
_max = scores[-1]

for i in range(N-2, -1, -1):
    if _max <= scores[i]:
        dif = scores[i] - _max -1
        count += dif
        _max = dif

print(count)