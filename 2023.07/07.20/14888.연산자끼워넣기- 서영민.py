def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if a < 0:
            return -(-a // b)
        else:
            return a // b

def backtrack(arr, idx, add, sub, mul, div, current_result):
    global max_result, min_result

    if idx == len(arr):
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    if add > 0:
        backtrack(arr, idx + 1, add - 1, sub, mul, div, current_result + arr[idx])

    if sub > 0:
        backtrack(arr, idx + 1, add, sub - 1, mul, div, current_result - arr[idx])

    if mul > 0:
        backtrack(arr, idx + 1, add, sub, mul - 1, div, current_result * arr[idx])

    if div > 0:
        backtrack(arr, idx + 1, add, sub, mul, div - 1, calculate(current_result, arr[idx], '/'))

N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = float('-inf')
min_result = float('inf')

backtrack(numbers, 1, add, sub, mul, div, numbers[0])

print(max_result)
print(min_result)

# N = int(input())

# numbers = list(map(int, input().split()))
# operator = list(map(int, input().split()))

# _max = -1e9
# _min = 1e9

# plus, minus, multiply, divide = operator


# def dfs(length, total, plus, minus, multiply, divide):
#     global _max, _min
#     if length == N:
#         if _max < total:
#             _max = total
#         if _min > total:
#             _min = total
#         return
            
#     if plus:
#         dfs(length+1, total+numbers[length], plus-1, minus, multiply, divide)    
    
#     if minus:
#         dfs(length+1, total-numbers[length], plus, minus-1, multiply, divide)
        
#     if multiply:
#         dfs(length+1, total*numbers[length], plus, minus, multiply-1, divide)
        
#     if divide:
#         dfs(length+1, int(total/numbers[length]), plus, minus, multiply, divide-1)
        
# dfs(1, numbers[0], plus, minus, multiply, divide)
    
# print(_max)
# print(_min)
    