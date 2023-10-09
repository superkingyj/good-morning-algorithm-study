import sys

N, L, W, H = map(int, sys.stdin.readline().split())

start, end = 0, max(L, W, H)

for _ in range(100):
    mid = (start + end) / 2
    count = (L // mid) * (W // mid) * (H // mid)
    if count >= N:
        start = mid
    else:
        end = mid
        
print(start)