import sys

N, M, L = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split())) + [L]
arr.sort()

# mid값의 거리로 M개의 휴게소를 놓을 수 있는지 확인하기
def is_possible(mid):
    cnt = 0
    
    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] > mid:
            cnt += (arr[i] - arr[i-1] -1) // mid
    
    return cnt <= M

def binary_search():
    left, right = 1, L
    result = sys.maxsize

    while left <= right:
        mid = (left+right) // 2
    
        if is_possible(mid):
            result = mid
            right = mid-1
        else:
            left = mid+1

    return result

print(binary_search())
