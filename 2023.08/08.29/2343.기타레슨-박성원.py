# https://www.acmicpc.net/problem/2343

n, m = map(int, input().split())
li = list(map(int, input().split()))
start = 0
end = 0

for i in li :
    if start < i :
        start = i
    end += 1

while start <= end :
    middle = int((start+end)/2)
    sum = 0
    count = 0
    for i in range(n) :
        if sum + li[i] > middle :
            count += 1
            sum = 0
        sum += li[i]
    if sum != 0 :
        count += 1
    if count > m :
        start = middle + 1
    else :
        end = middle - 1

print(start)

