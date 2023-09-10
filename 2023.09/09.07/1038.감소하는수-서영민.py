N = int(input())

numbers = []


def dfs(depth, res):
    
    if depth > 10:
        return
    
    for i in range(10):
        temp = res
        res += str(i)
        if len(res) == 1:
            numbers.append(int(res))
            dfs(depth+1, res)
        elif res[-2] > res[-1]:
            numbers.append(int(res))
            dfs(depth+1, res)
        res = temp
dfs(1, '')
numbers.sort()

if N < len(numbers):
    print(numbers[N])
else:
    print(-1)
    
    