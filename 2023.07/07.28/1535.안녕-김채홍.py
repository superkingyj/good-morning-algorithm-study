import sys

input = sys.stdin.readline

N = int(input())                    #첫째 줄에 사람의 수 N
L = list(map(int, input().split())) #둘째 줄에는 각각의 사람에게 인사를 할 때, 잃는 체력 
J = list(map(int, input().split())) # 셋째 줄에는 각각의 사람에게 인사를 할 때, 얻는 기쁨 

L = [0] + L #배열에 저장 
J = [0] + J #배열에 저장

#i번째 사람에게 인사를 하고, 스테미너 소모량보다 체력 j가 클 때 인사를 해서 얻을 수 있는 기쁨의 양을 계산하여 dp에 저장
dp = [[0 for _ in range(101)] for _ in range(N+1)] 

for i in range(1, N+1):
    for j in range(1, 101):
        if L[i] <= j: #dp[i][j] 는 dp[i-1][j]의 값을 가져다 넣는 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][99])