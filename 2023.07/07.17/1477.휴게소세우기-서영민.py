N, M, L = map(int, input().split())


r = [0] + list(map(int, input().split())) + [L]
r.sort()
start, end = 1, L-1

while start <= end:
    mid = (start+end)//2
    count = 0
    for i in range(1, len(r)):
        temp = (r[i] - r[i-1])
        if temp > mid:
            count += (temp-1)//mid
    
    if  count > M:
        start = mid+1
    else:
        end = mid-1

print(start)