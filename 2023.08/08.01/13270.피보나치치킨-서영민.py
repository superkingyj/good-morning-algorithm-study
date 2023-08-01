def fibo(N, first, second):
    dp = [0] * (N+1)
    dp[1] = first
    dp[2] = second
    
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp
N = int(input())

people = fibo(14, 2, 3)
chicken = fibo(14, 1, 2)


min_chicken = 1000
max_chicken = 0
for idx, p in enumerate(people):
    if idx != 0:
        if N % p == 0:
            min_chicken = min(min_chicken, chicken[idx]*(N/p))


max_dp = [0]* (7)
max_dp[2] = 1
max_dp[3] = 2
max_dp[4] = 2
max_dp[5] = 3
max_dp[6] = 4   

if N >6 :
    max_dp = max_dp + [0]*(N-6)  

for i in range(7, N+1):
    idx = 2
    while max_dp[idx] < N:
        max_dp[i] = max(max_dp[i], max_dp[i]+ max_dp[i-max_dp[idx]])
        idx += 1

print(int(min_chicken), max_dp[N])    

