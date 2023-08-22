import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())

# 소수 판별 함수
def isprime(num):
    for i in range(2, int(num ** (1 / 2) + 1)):
        if num % i == 0:
            return False
    else:
        return True

def recursive(n):
    if len(str(n)) == N:
        print(n)
    else:
        # 홀수만 붙여서 소수 판별
        for i in range(1, 10, 2):
            temp = 10 * n + i
            if isprime(temp):
                recursive(temp)
            
prime = [2, 3, 5, 7]

for i in prime:
    recursive(i)