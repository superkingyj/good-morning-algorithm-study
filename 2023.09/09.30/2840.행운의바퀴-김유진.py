import sys

N, K = map(int, sys.stdin.readline().split())
circle = ['?'] * N
flag = True
result = '!'

for _ in range(K):
    input = sys.stdin.readline().split()
    S, char = int(input[0]) % N, input[1]
    # 왜 이렇게 해야함?
    circle = circle[-S:] + circle[:-S]
    
    if circle[0] == '?':
        if char in circle:
            flag = False
            break
        else:
            circle[0] = char
    elif circle[0] == char:
        pass 
    else:
        flag = False
        break

if flag: result = ''.join(circle)
print(result)