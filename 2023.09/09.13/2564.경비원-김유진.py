import sys

M, N = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
stores = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
dk = tuple(map(int, sys.stdin.readline().split()))
total_dist = 0

# 동근이가 북쪽에 있는 경우
if dk[0] == 1:  
    for dir, dist in stores:
        if dir == 1:
            total_dist += abs(dk[1] - dist)
        elif dir == 2:
            left_way = dk[1] + N + dist
            right_way = (M - dk[1]) + N + (M - dist)
            total_dist += min(left_way, right_way)
        elif dir == 3:
            total_dist += dk[1] + dist
        elif dir == 4:
            total_dist += (M - dk[1]) + dist
# 동근이가 남쪽에 있는 경우
elif dk[0] == 2:  
    for dir, dist in stores:
        if dir == 1:
            left_way = dk[1] + N + dist
            right_way = (M - dk[1]) + N + (M - dist)
            total_dist += min(left_way, right_way)
        elif dir == 2:
            total_dist += abs(dk[1] - dist)
        elif dir == 3:
            total_dist += dk[1] + (N - dist)
        elif dir == 4:
            total_dist += (M - dk[1]) + (N - dist)
# 동근이가 서쪽에 있는 경우
elif dk[0] == 3:  
    for dir, dist in stores:
        if dir == 1:
            total_dist += dk[1] + dist
        elif dir == 2:
            total_dist += (N - dk[1]) + dist
        elif dir == 3:
            total_dist += abs(dk[1] - dist)
        elif dir == 4:
            left_way = dk[1] + M + dist
            right_way = (N - dk[1]) + M + (N - dist)
            total_dist += min(left_way, right_way)
# 동근이가 동쪽에 있는 경우
elif dk[0] == 4:  
    for dir, dist in stores:
        if dir == 1:
            total_dist += dk[1] + (M - dist)
        elif dir == 2:
            total_dist += (N - dk[1]) + (M - dist)
        elif dir == 3:
            left_way = (N - dk[1]) + M + (N - dist)
            right_way = dk[1] + M + dist
            total_dist += min(left_way, right_way)
        elif dir == 4:
            total_dist += abs(dk[1] - dist)

print(total_dist)