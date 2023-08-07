import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def paramatric_search(left, right):
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        limit = mid
        budget = 0

        for i in range(N):
            if arr[i] >= limit:
                budget += limit
            else:
                budget += arr[i]
        
        if budget <= max_budget:
            answer = limit
            left = mid+1
        else:
            right = mid-1

    return answer

left = 0
max_budget = int(sys.stdin.readline())
right = max(arr)
print(paramatric_search(left, right))