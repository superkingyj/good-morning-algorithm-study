from sys import stdin
input = stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))

start, end = 0, N-1
ans = abs(arr[start]+arr[end])
final = [arr[start], arr[end]]

while start < end:
    left = arr[start]
    right = arr[end]

    sum = left + right

    if abs(sum) < ans:
        ans = abs(sum)
        final = [left, right]
        if ans == 0:
            break

    if sum < 0:
        start += 1 
    else:
        end -= 1  
print(final[0], final[1])