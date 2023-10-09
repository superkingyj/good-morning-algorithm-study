import sys
input = sys.stdin.readline

N, L, W, H = map(int, input().split())

max_length = min(L, W, H)

min_length = 0

target = L * W * H

for _ in range(10000):
    mid = (min_length + max_length)/2
    count = (L // mid) * (W // mid) * (H // mid)
    
    if count >= N:
        min_length = mid 
    else:
        max_length = mid
        

print("%.10f" %(max_length))