import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

saqik = list(map(int, sys.stdin.readline().split()))

maxnum = -1e9
minnum = 1e9


def dfs(depth, total, add, minus, multiply, divide):
    global maxnum, minnum
    
    
    # 숫자를 다 사용했다면 maxnum과 minnum 지정
    if depth == N:
        maxnum = max(total, maxnum)
        minnum = min(total, minnum)
    
    # 사칙연산별로 해당하는 것들을 사용해서 재귀적으로 계산하기
    
    if add:
        dfs(depth + 1, total + arr[depth], add - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - arr[depth], add, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * arr[depth], add, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / arr[depth]), add, minus, multiply, divide - 1)    
            
dfs(1, arr[0], saqik[0], saqik[1], saqik[2], saqik[3])

print(maxnum)
print(minnum)

    