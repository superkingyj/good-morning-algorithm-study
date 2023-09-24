# https://www.acmicpc.net/problem/1874

import sys
input = sys.stdin.readline

n = int(input())
stack = [] # 입력값에 주어진 스택을 관리하기 위함
answer = [] # +, - 를 담을 리스트

current = 1 # 마지막에 갖고 있던 수
flag = 0

for _ in range(n) :
    num = int(input())

    # stack이 추가될때
    while current <= num :
        stack.append(current)
        answer.append('+')
        current += 1

    # stack이 제거될때
    if stack[-1] == num :
        stack.pop()
        answer.append('-')
    else :
        print('NO')
        flag = 1
        break

if flag == 0 :
    for i in answer :
        print(i)