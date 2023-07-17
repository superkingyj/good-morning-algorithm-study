import sys

D, K = map(int, sys.stdin.readline().split())
num1, num2, flag = 0, 0, False

def dynamic_programming(i, j):
    DP = [0] * (D+1)
    DP[1], DP[2] =i, j
    
    for i in range(3, D+1):
        DP[i] = DP[i-1]+DP[i-2]
    
    return DP


for i in range(1, 100000):
    for j in range(1, 100000):
        DP = dynamic_programming(i,j)
        
        if DP[-1] == K:
            num1, num2 = DP[1], DP[2]
            flag = True
            break
    
    if flag: break

print(num1)
print(num2)