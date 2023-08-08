n = int(input())

money = list(map(int, input().split()))

target = int(input())

left, right = 1, max(money)

while left <= right:
    
    mid = (left+right)//2
    
    total = 0
    for i in money:
        if i <= mid:
            total += i
        else:
            total += mid
    
    if total <= target:
        left = mid +1
    else:
        right = mid-1
print(right)