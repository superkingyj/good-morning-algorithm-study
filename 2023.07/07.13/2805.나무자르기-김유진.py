import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# mid값으로 M미터 이상의 나무를 가져갈 수 있는지 확인
def is_possible(mid):
    sum_val = 0
    for i in range(N):
        if arr[i] <= mid: continue
        sum_val += (arr[i]-mid)
    return sum_val >= M
    

def binary_search():
    left, right = 0, max(arr)+1
    result = -sys.maxsize
    
    while left <= right:
        mid = (left+right) // 2
        
        if is_possible(mid):
            result = max(result, mid)
            left = mid+1
        else:
            right = mid-1
    
    return result

print(binary_search())