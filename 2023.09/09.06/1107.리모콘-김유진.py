import sys

target = int(sys.stdin.readline())
M = int(sys.stdin.readline())
nums = set(i for i in range(10))

if M > 0:
    not_working = set(sys.stdin.readline().split())
else:
    not_working = set()
    
min_cnt = abs(target - 100)

for i in range(1000001):
    flag = True
    
    # 만약 i안의 숫자가 not_working안에 있다면 break
    for j in str(i):
        if j in not_working:
            flag = False
            break

    # len(str(i)) : 해당 숫자 i를 누르는데 필요한 횟수
    # abs(target - i) : i에서 target까지 이동하는데 필요한 횟수
    if flag: min_cnt = min(min_cnt, len(str(i)) + abs(target - i))
    
print(min_cnt)
