n = int(input())
price = [0] + list(map(int, input().split()))

dp = [0] * (n+1)


print(price)
print(dp)

for i in range(1,n+1) :
    for j in range(1,n+1):
        dp[i] = max(dp[i], dp[i-j] + price[j])

print(dp)
