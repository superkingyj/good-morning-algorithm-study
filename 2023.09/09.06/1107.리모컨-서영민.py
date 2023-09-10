import sys

input = sys.stdin.readline

target = list(input().rstrip())

N = int(input())

arr = []

if N > 0:
    arr = list(map(int, input().split()))

res = []
temp = int("".join(target))
for i in range(len(target)):
    if i not in arr:
        res.append(i)
    else:
        n = 0
        number = [sys.maxsize, -1]
        while n < 10:
            if n not in arr:
                temp2 = res + [n]
                temp2 = int("".join(temp2)) * (10 ** (len(target) - i + 1))
                if number[0] > abs(temp2 - temp):
                    number[0] = abs(temp2 - temp)
                    number[1] = i
            n += 1
        if number[1] != -1:
            res += str(number[1])
            break
    res = int(res)
if temp == 100:
    print(0)
else:
    res = abs(res-temp-100)
    print(min(res, temp - 100))