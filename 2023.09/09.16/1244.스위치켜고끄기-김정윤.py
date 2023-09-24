import sys

switch_num = int(sys.stdin.readline())

switch = [-1] + list(map(int, sys.stdin.readline().split()))

student_num = int(sys.stdin.readline())

def turnswitch(idx):
    if switch[idx - 1]:
        switch[idx - 1] = 0
    else:
        switch[idx - 1] = 1

for i in range(student_num):
    sex, num = map(int, sys.stdin.readline().split())
    if sex == 1:
        for j in range(num, switch_num + 1, num):
            turnswitch(num * i)
    else:
        turnswitch(num)
        for j in range(switch_num // 2):
            if num + j > switch_num or num - j < 1:
                break
            if switch[num + j] == switch[num - j]:
                turnswitch[num + j]
                turnswitch[num - j]
                
            else:
                break
            
for i in range(1, switch_num + 1):
    print(switch[i], end = ' ')
    if not i % 20:
        print()