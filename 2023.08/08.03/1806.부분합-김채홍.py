import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))
target = 0
left = 0
right = 0
answer = 1000001


while True:
    if target >= S:
        answer = min(answer, right - left) 
        target -= arr[left] 
        left += 1 
    else:

        if right == N:
            break
        
        target += arr[right] 
        right += 1 

print(0) if answer == 1000001 else print(answer)