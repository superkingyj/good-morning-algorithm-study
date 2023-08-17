from bisect import bisect_left as b_left
import sys

input = sys.stdin.readline

k = int(input())

switches = list(map(int, input().split()))
bulbs = list(map(int, input().split()))

arr = []

for i in range(k):
    arr.append((bulbs.index(switches[i]), switches[i]))
    
def getLis():
    dp = [arr[0][0]]
    Lis = [(0, arr[0][1])]
    
    for i in range(1, k):
        idx, switch = arr[i]
        
        if idx > dp[-1]:
            dp.append(idx)
            Lis.append((len(dp)-1, switch))
        else:
            dpidx = b_left(dp, idx)
            dp[dpidx] = idx
            Lis.append((dpidx, switch))
    return len(dp), Lis

Lis_length, Lis = getLis()

print(Lis_length)

count = Lis_length - 1
res = [0 for _ in range(Lis_length)]

print(Lis)
for (idx, value) in reversed(Lis):
    if count == idx:
        res[idx] = value
        count -= 1
        
    if count < 0:
        break

res.sort()
print(*res)