import sys

N = int(sys.stdin.readline())

ch_list = list(map(int, sys.stdin.readline().split()))

ch_list.sort()
left = 0
right = N - 1
result = sys.maxsize

while left < right:
    temp = ch_list[left] + ch_list[right]
    if abs(temp) <= result:
        result = temp
        result_left = left
        result_right = right
    
    if temp == 0:
        break
    if temp < 0:
        left += 1
    else:
        right -= 1
print(ch_list[result_left], ch_list[result_right])
    