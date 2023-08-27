# https://www.acmicpc.net/problem/1541

# 최초로 마이너스가 나오기 전까지 나오는 수자는 모두 더하고, 이후 마이너스가 나오는 순간 그 뒤에 있는 모든 수를 뺀다.
# 연속해서 두 개 이상의 연산자가 나타나지 않는다.

s = input().split('-')
result = 0

for i in s[0].split('+') :
    result += int(i)

for i in s[1:] :
    for j in i.split('+') :
        result -= int(j)

print(result)
