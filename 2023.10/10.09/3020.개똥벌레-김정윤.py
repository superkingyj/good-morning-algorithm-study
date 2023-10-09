import sys

N, H = map(int, sys.stdin.readline().split())
석순 = [0] * (H + 1)
종유석 = [0] * (H + 1)

cnt = N
result = 0

for i in range(N):
    if i % 2 == 0:
        석순[int(sys.stdin.readline())] += 1
    else:
        종유석[int(sys.stdin.readline())] += 1
    
for i in range(H - 1, 0, -1):
    석순[i] += 석순[i + 1]
    종유석[i] += 종유석[i + 1]
    
for i in range(1, H + 1):
    if cnt > (석순[i] + 종유석[H - i + 1]):
        cnt = (석순[i] + 종유석[H - i + 1])
        result = 1
    elif cnt == (석순[i] + 종유석[H - i + 1]):
            result += 1

print(cnt, result)