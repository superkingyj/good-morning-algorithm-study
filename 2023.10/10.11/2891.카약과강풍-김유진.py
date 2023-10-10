import sys

N, S, R = map(int, input().split())

broken = list(map(int, input().split()))  # 카약이 손상된 팀
extra = list(map(int, input().split()))  # 카약이 남는 팀

result = S  # 출발하지 못하는 팀 수

for kayak in extra:
    if kayak in broken:
        extra.remove(kayak)
        broken.remove(kayak)
        result -= 1

for broken_kayak in broken:
    for extra_kayak in extra:
        if extra_kayak - 1 <= broken_kayak <= extra_kayak + 1:
            extra.remove(extra_kayak)
            result -= 1
            break

print(result)
