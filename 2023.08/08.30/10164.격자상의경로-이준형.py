from sys import stdin

input = stdin.readline

def find(y,x):
    dp = [[0 for _ in range(x+1)] for _ in range(y+1)]
    
    for i in range(1, y+1):
        for j in range(1, x+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
                continue
            
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[y][x]

def main():
    N,M,K = map(int, input().split())
    if K == 0:
        return find(N,M)
        
    S_N1 = (K-1)//M+1
    S_M1 = K - (S_N1-1)*M
    S_N2 = N - (S_N1-1)
    S_M2 = M - (S_M1-1)
    
    res1 = find(S_N1,S_M1)
    res2 = find(S_N2,S_M2)
    
    return res1*res2

if __name__=="__main__":
    res = main()
    print(res) 