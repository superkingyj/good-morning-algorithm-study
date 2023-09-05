import sys, bisect

N = int(sys.stdin.readline())

S = list(map(int, sys.stdin.readline().split()))
L = list(map(int, sys.stdin.readline().split()))
SL = [0] * (N + 1)

for idx, val in enumerate(L):
    SL[val] = idx + 1

LIS = []
TRACE = []

for l in S:
    sl = SL[l]
    if not LIS or LIS[-1] < l:
        TRACE.append(len(LIS))
        LIS.append(sl)
    else:
        idx = bisect.bisect_left(LIS, sl)
        LIS[idx] = sl
        TRACE.append(idx)

print(len(LIS))
print(*LIS)
