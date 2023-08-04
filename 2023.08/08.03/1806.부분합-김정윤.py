import sys

N, S = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
target = 0
left = 0
right = 0
result = 1000000000001

while True:
    # 총 합이 S가 넘는다면 left를 하나씩 옮기면서 길이 확인
    if target >= S:
        # 길이를 result에 저장
        result = min(result, right - left)
        target -= arr[left]
        left += 1
    # S가 넘지 않는다면 right를 오른쪽으로 하나씩 옮기면서 S를 넘길 때까지 더함
    else:
        # right가 맨 오른쪽에 도달하면 break
        if right == N:
            break
        target += arr[right]
        right += 1

if result == 1000000000001:
    print(0)
else:
    print(result)
