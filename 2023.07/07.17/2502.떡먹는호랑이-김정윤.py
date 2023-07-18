import sys

D, K = map(int, sys.stdin.readline().split())

arr = [0] * D

arr[0], arr[1] = 1, 1

while True:
    for i in range(2, D):
        arr[i] = arr[i - 1] + arr[i - 2]
    
    # 마지막 값이 K 값과 일치한다면, 0과 1 출력
    if arr[-1] == K:
        print(arr[0])
        print(arr[1])
        break
    # 마지막 값이 K보다 크다면, 새로운 수로 대입하기 위해 1 증가
    elif arr[-1] > K:
        arr[0] += 1
        arr[1] = arr[0]
    else:
        arr[1] += 1