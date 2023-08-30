import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

candidates = dict()

for idx, num in enumerate(arr):
    # 사진이 걸려있는 경우
    if num in candidates:
        candidates[num][0] += 1    
    # 비어있는 사진 틀이 있는 경우
    elif len(candidates) < N:
        candidates[num] = [1, idx]
    # 비어있는 사진 틀이 없는 경우
    else:
        # 추천수가 가장 적은 학생 삭제
        target = sorted(candidates.items(), key = lambda x: (x[1][0], x[1][1]))[0]
        del candidates[target[0]]
        candidates[num] = [1, idx]

print(*sorted(list(candidates.keys())))