import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def is_possible(mid):
    cnt = 1
    curr_val = 0
    
    for num in arr:
        if curr_val + num > mid:
            cnt += 1
            curr_val = num
        else:
            curr_val += num
    
    return cnt <= M


def brinary_search():
    left, right = max(arr), sum(arr)+1
    result = sys.maxsize
    
    while left <= right:
        mid = (left + right) // 2
        
        if is_possible(mid):
            result = min(result, mid)
            right = mid - 1
        else:
            left = mid + 1
    
    return result

print(brinary_search())