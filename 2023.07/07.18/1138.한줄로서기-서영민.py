N = int(input())
talls = list(map(int, input().split()))
result = [0]*(N)

for i in range(1,N+1):
    count = 0
    watch = talls[i-1]
    for k in range(N):
        if count == watch and result[k] == 0:
            result[k] = i
            break
        elif result[k] == 0:
            count += 1
            
print(*result)
    