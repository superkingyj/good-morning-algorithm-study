import sys

def 거리찾기(상점, 위치):
    if 상점 == 1:
        return 위치
    if 상점 == 2:
        return 2 * 가로 + 세로 - 위치
    if 상점 == 3:
        return 2 * 가로 + 2 * 세로 - 위치
    if 상점 == 4:
        return 가로 + 위치

가로, 세로 = map(int, sys.stdin.readline().split())
상점개수 = int(sys.stdin.readline())

arr = []

for i in range(상점개수 + 1):
    상점, 위치 = map(int, sys.stdin.readline().split())
    arr.append(거리찾기(상점, 위치))
    

결과 = 0

for i in range(상점개수):
    inside = abs(arr[-1] - arr[i])
    outside = 2 * (가로 + 세로) - inside
    결과 += min(inside, outside)
    
print(결과)
