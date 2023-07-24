import sys

N, X = map(int, sys.stdin.readline().split())

hamburger = [1] * (N + 1)
patty = [1] * (N + 1)

def countpatty(N, X):
    if N == 0:
        if X == 0:
            return 0
        else: return 1
    
    # 레벨 1부터 주문가능한데, N이 어떤 수이든 X가 1이면 패티는 0장
    if X == 1:
        return 0
    
    # X가 중간패티 위치보다 작다면 앞의 번을 빼고 이전 레벨의 햄버거 패티 수 호출
    # X - 1을 해주는 이유는 번의 개수가 레벨이 내려가면 하나가 적어지기 때문
    elif X <= 1 + hamburger[N - 1]:
        return countpatty(N - 1, X - 1)

    # X가 중간 패티 위치라면 이전 패티수 + 1 반환
    # 패티 + 이전버거 + 번으로 중간 개수 찾음 
    elif X == 2 + hamburger[N - 1]:
        return patty[N - 1] + 1
    
    # X가 중간 패티 위치보다 크다면
    elif X <= 2 + 2 * hamburger[N - 1]:
        # 중간 패티수 까지 계산 후 이전 버거의 추가적인 패티 계산
        # 추가 패티 계산을 할 때는 X에서 중간 패티수까지 계산한 값을 빼주고 돌려줌
        return patty[N - 1] + 1 + countpatty(N - 1, X - (2 + hamburger[N - 1]))
    
    # X가 현재 레벨 햄버거와 동일하다면 현재 레벨 패티 수 반환
    else:
        return 2 * patty[N - 1] + 1

# N레벨 까지 전체 재료수와 패티수 구함
# 버거의 경우 2개의 햄버거번(1), 2개의 레벨 L-1버거(hamburger[i - 1]), 1개의 패티(1)를 더해주면 됨
# 패티의 경우 2개의 레벨 L - 1 버거의 패티(patty[i - 1]), 1개의 패티(1)를 더해주면 됨
for i in range(1, N + 1):
    hamburger[i] = 3 + 2 * hamburger[i - 1]
    patty[i] = 1 + 2 * patty[i - 1]
    
print(countpatty(N, X))