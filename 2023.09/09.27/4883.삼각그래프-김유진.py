import sys

test_case_number = 1

while True:
    N = int(sys.stdin.readline())
    if N == 0: break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    DP = [[sys.maxsize] * 3 for _ in range(N)]
    DP[1][0] = arr[1][0] + arr[0][1]
    DP[1][1] = arr[1][1] + min(DP[1][0], arr[0][1], arr[0][1]+arr[0][2])
    DP[1][2] = arr[1][2] + min(DP[1][1], arr[0][1], arr[0][1]+arr[0][2])
    
    for i in range(2, N):
        for j in range(3):
            if j == 0: min_val = min(DP[i-1][j], DP[i-1][j+1])
            elif j == 1: min_val = min(DP[i-1][j-1], DP[i-1][j], DP[i-1][j+1], DP[i][j-1])
            else: min_val = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1])
            DP[i][j] = arr[i][j] + min_val
    
    print(f"{test_case_number}. {DP[-1][1]}")
    test_case_number += 1    


