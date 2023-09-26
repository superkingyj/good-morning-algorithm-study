A, B, C = map(int, input().split())

# 분할정복
def solve(a, b):
    if b == 1:  # b의 값이 1이 될 때까지 재귀
        return a % C
    else:
        tmp = solve(a, b // 2)  # a^(b // 2)
        if b % 2 == 0:
            return tmp * tmp % C  # b가 짝수인 경우
        else:
            return tmp * tmp * a % C  # b가 홀수인 경우

res = solve(A, B)
print(res)
