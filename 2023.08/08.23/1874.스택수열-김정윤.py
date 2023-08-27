import sys

N = int(sys.stdin.readline())
arr = []
result = []
start = 0

for i in range(N):
    val = int(sys.stdin.readline())
    if val > start:
        for i in range(start + 1, val + 1):
            arr.append(i)
            result.append('+')
        start = val
    
    elif (arr[-1] != val):
        result.append('NO')
        break
    
    arr.pop()
    result.append('-')
    
if result.count('NO') == 1:
    print('NO')
else:
    for i in result:
        print(i)
            