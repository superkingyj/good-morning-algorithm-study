N = int(input())
numbers = list(map(int, input().split()))

nge_result = [-1] * N 

stack = []  

for i in range(N-1, -1, -1):
    while stack and numbers[i] >= numbers[stack[-1]]:
        stack.pop()
    
    if stack:  
        nge_result[i] = numbers[stack[-1]]
    
    stack.append(i)

print(*nge_result)