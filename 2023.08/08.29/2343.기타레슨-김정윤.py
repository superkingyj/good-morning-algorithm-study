import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def count_video(list, mid):
    cnt = 1
    lecture_length = 0
    for i in list:
        if lecture_length + i > mid:
            cnt += 1
            lecture_length = i
        else:
            lecture_length += i
    return cnt

left = max(arr)
right = sum(arr)

while left <= right:
    mid = (left + right) // 2
    
    if count_video(arr, mid) <= M:
        right = mid - 1
    else:
        left = mid + 1

print(left)