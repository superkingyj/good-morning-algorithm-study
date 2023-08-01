import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

prefix = [0] * (N+1)
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + arr[i-1]

result, left, right = 100001, 0, 1

while left < N:
    if prefix[right] - prefix[left] >= S:
        result = min(result, right-left)
        left += 1
    else:
        if right < N: right += 1
        else: left += 1
    
print(result if result != 100001 else 0)