import sys

n, m, l = map(int, sys.stdin.readline().split())

li = [0] + list(map(int, sys.stdin.readline().split())) + [l]
li.sort()

start = 1
end = l -1
ans = 0

while start <= end :
    middle = (start+end) // 2
    count = 0
    
    for i in range(1, len(li)) :
        if li[i] - li[i-1] > middle :
            count += (li[i] - li[i-1] -1)//middle

    if count > m :
        start = middle + 1
    else :
        end = middle - 1
        ans = middle

print(ans)