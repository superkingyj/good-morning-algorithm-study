import sys

input = sys.stdin.readline

n, s = map(int, input().split())

numbers = list(map(int, input().split()))


plus, minus = 0, 0

sum = 0
length = sys.maxsize

while True:
    if sum >= s:
        sum -= numbers[minus]
        minus += 1
        length = min(length, plus-minus+1)
    elif plus == n:
        break
    else:
        sum += numbers[plus]
        plus += 1
        
if length == sys.maxsize:
    print(0)
else:
    print(length)