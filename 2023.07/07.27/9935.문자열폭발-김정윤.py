import sys
from collections import deque

str = sys.stdin.readline().rstrip()

bomb_str = sys.stdin.readline().rstrip()

stack = []


for i in str:
    stack.append(i)
    # i가 stack 배열의 끝부분이면서, bomb_str 길이만큼 붙였을 때 bomb_str이라면, stack에서 삭제
    # ex) vC 다음 stack[-len(bomb_str):]은 'C','4'인데 그것을 ''.join()으로 붙여서 C4가 되는데 C4가 터져서 없어짐
    if i == stack[-1] and ''.join(stack[-len(bomb_str):]) == bomb_str:
        # del을 쓰지 않고 폭탄 문자열 길이만큼 반복해서 pop해도 상관 없음
        del stack[-len(bomb_str):]

# 글자 문자열로 결합   
result = ''.join(stack)

if result == '':
    print("FRULA")

else: print(result)
        