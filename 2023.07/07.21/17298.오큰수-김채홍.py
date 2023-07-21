#스택 O(n)

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

stack = []
answer = [-1 for i in range(n)]

for i in range(len(array)):
    #스택의 마지막 array값이 비교하는 값보다 작다면 오른쪽 큰수로 설정
    while stack and array[stack[-1]] < array[i]:
        answer[stack.pop()] = array[i]
    stack.append(i)
print(*answer)