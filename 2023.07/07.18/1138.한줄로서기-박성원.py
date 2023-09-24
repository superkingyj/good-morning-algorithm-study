import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

# 좌석 설정
ans = [0] * n

# 입장한 사람
for i in range(n):
    count = 0
    
    # 자리를 찾는 중
    for j in range(n):
        # li[i] : 자기 앞에 있어야 될 사람의 수 / ans[j] : 자리가 비어있는지 확인
        if count == li[i] and ans[j] == 0:
            ans[j] = i + 1
            break
        # 자리가 비어 있다면 앞에 있어야 될 사람의 수가 충족되지 않기 때문에 i를 추가
        elif ans[j] == 0:
            count += 1

# 언팩킹해서 출력
print(*ans)
