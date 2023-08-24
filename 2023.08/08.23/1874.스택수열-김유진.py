import sys

N = int(sys.stdin.readline())
stack = []
curr_num = 1
result = []
flag = True

for _ in range(N):
    input_num = int(sys.stdin.readline())
    
    while curr_num <= input_num:
        stack.append(curr_num)
        result.append("+")
        curr_num += 1
    
    if stack[-1] != input_num:
        flag = False
        break

    stack.pop()
    result.append("-")

if not flag:
    print("NO")
else:
    for op in result:
        print(op)