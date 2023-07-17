import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
hugae = list(map(int, input().split()))

hugae.append(0)
hugae.append(L-1)
hugae = sorted(hugae)

left = 0
right = L-1
while left <= right:
    mid = (left+right) // 2
    count = 0 
    for i in range(1, len(hugae)):
        if hugae[i] - hugae[i-1] > mid:
            count += (hugae[i] - hugae[i-1] -1)//mid

    if count > M:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)