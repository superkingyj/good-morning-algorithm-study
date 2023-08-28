import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lecture = list(map(int, input().split()))

left, right = max(lecture), sum(lecture)

while left <= right:
    
    mid = (left + right)//2
    
    count = 1
    temp = 0
    for i in lecture:
        if temp + i <= mid:
            temp += i
        else:
            temp = i
            count += 1
        if count > M:
            break
    
    if count > M:
        left = mid + 1
    else:
        right = mid - 1
        
print(left)