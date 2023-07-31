import sys

N = int(sys.stdin.readline())

fibo = [0] * 1000000
fibo[0] = 0
fibo[1] = 1
fibo[2] = 2
    
for i in range(2, N+1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

def get_min():
    min_val, n = 0, N
    # 홀수면 3마리 추가
    if n % 2 == 1:
        n -= 3
        min_val += 2
    
    min_val += n // 2
    return min_val

def get_max():
    DP = [0] * 1000000
    DP[2] = 1
    DP[3] = 2
    DP[4] = 2
    DP[5] = 3
    DP[6] = 4

    for i in range(7, N + 1):
        curr_max, idx = -1, 2
        while fibo[idx] <= i:
            curr_max = max(curr_max, DP[fibo[idx]] + DP[i - fibo[idx]])
            idx += 1
        DP[i] = curr_max
    
    return DP[N]

print(get_min(), get_max())
