import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

result = [0] * N

for i in range(N):
    # 왼쪽 키 큰 사람 수 체크
    cnt = 0
    for j in range(N):
        # 수가 맞고 그 자리에 아무도 없으면 추가
        if cnt == arr[i] and result[j] == 0:
            result[j] = i + 1
            break
        
        # 자리에 아무도 없으면 왼쪽에 키 큰 사람 수 확인
        elif result[j] == 0:
            cnt += 1

print(*result) 
            