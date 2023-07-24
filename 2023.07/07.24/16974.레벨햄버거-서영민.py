N, X = map(int, input().split())

burn = [0 for _ in range(N)]
patty = [0 for _ in range(N)]

burn[0] = 1
patty[0] = 1

for i in range(1, N):
    burn[i] = burn[i-1]*2 + 3
    patty[i] = patty[i-1]*2 + 1
    
def eat(n, x):      
    if n == 0:
        return x
    if x == 1:
        return 0
    elif x <= 1 + burn[n-1]:					
        return eat(n-1, x-1)             
    elif x == 1 + burn[n-1] + 1:               
        return patty[n-1] + 1
    elif x <= burn[n-1] + burn[n-1] + 1 + 1:	
        return patty[n-1] + 1 + eat(n-1, (x-(burn[n-1]+2)))
    else:										
        return patty[n]

print(eat(N, X))