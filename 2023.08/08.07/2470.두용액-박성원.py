# https://www.acmicpc.net/problem/2470
# queue를 써야하나? -> 용액 2개를 출력해야하기때문에

n = int(input())
li = list(map(int, input().split()))
li.sort()

left = 0
right = n-1

answer = abs(li[left] + li[right])
final = [li[left], li[right]]

while left < right :
    left_val = li[left]
    right_val = li[right]

    sum = left_val + right_val
    if abs(sum) < answer :
        answer = abs(sum)
        final = [left_val, right_val]
        if answer == 0 :
            break

    if sum < 0 :
        left += 1
    else :
        right -= 1

print(*final)