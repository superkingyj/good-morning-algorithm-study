import sys
N, X = map(int, sys.stdin.readline().split())

# i-level 버거의 총 레이어 수
burger = [1] * 51
# i-level 버거의 총 패티 수
patty = [1] * 51

def make_burger():
    for i in range(1, N+1):
        burger[i] = 1 + burger[i-1] + 1 + burger[i-1] + 1
        patty[i] = patty[i-1] + 1 + patty[i-1]

def eat(n, x):
    if n == 0:
        return x
    if x == 1:
        return 0
    elif x <= 1 + burger[n-1]:
        return eat(n-1, x-1)
    elif x == 1 + burger[n-1] + 1:
        return patty[n-1] + 1
    elif x <= burger[n-1] + burger[n-1] + 1 + 1:
        return patty[n-1] + 1 + eat(n-1, (x-(burger[n-1]+2)))
    else:
        return patty[n]

make_burger()
print(eat(N, X))