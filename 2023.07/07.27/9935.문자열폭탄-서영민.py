import sys

string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []
bomb_length = len(bomb)

for i in string:
    stack.append(i)
    if ''.join(stack[-bomb_length:]) == bomb:
        for _ in range(bomb_length):
            stack.pop()
            
if stack:
    print(''.join(stack))
else:
    print("FRULA")
