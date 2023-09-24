import sys

N = int(sys.stdin.readline())
switch = [0] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
student = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

for gender, num in student:
    # 남 - num의 배수에 해당하는 번호의 스위치를 바꿈
    if gender == 1:
        for i in range(num, N+1, num):
            switch[i] = int(not switch[i])
    # 여 - num을 중심으로 양쪽의 스위치의 상태가 같을 때까지 스위치를 바꿈
    else:
        switch[num] = int(not switch[num])
        left, right = num-1, num+1
        while 1 <= left and right <= N and switch[left] == switch[right]:
            switch[left] = int(not switch[left])
            switch[right] = int(not switch[right])
            left -= 1
            right += 1

for i in range(1, N+1, 20):
    print(*switch[i:i+20])