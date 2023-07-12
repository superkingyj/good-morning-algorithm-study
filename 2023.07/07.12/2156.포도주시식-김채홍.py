a = int(input())
wines = []
for i in range(a):
    wines.append(int(input()))



for dp in range(3, a):
    dp[i] = max(dp[i-3]+wines[i-1]+wines[i], dp[i-2]+wines[i], dp[i-1])
    
print(max[a])