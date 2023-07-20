import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
min_result = sys.maxsize
max_result = -sys.maxsize

def cal(op, num1, num2):
    if op == "+": return num1 + num2
    if op == "-": return num1 - num2
    if op == "*": return num1 * num2
    if op == "/": return int(num1/num2)

def backtrackng(idx, val):
    global min_result, max_result
    
    if idx >= N:
        min_result = min(min_result, val)
        max_result = max(max_result, val)
        return
    
    num1 = val
    num2 = arr[idx]

    if op[1] > 0:
        op[1] -= 1
        backtrackng(idx+1, cal("-", num1, num2))
        op[1] += 1
    if op[3] > 0:
        op[3] -= 1
        backtrackng(idx+1, cal("/", num1, num2))
        op[3] += 1
    if op[0] > 0:
        op[0] -= 1
        backtrackng(idx+1, cal("+", num1, num2))
        op[0] += 1
    if op[2] > 0:
        op[2] -= 1
        backtrackng(idx+1, cal("*", num1, num2))
        op[2] += 1 
        
backtrackng(1, arr[0])
print(max_result)
print(min_result)