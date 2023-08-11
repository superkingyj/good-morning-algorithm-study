import sys

N = int(sys.stdin.readline())

# 최대 공약수 구하기
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    temp = gcd(arr[0], arr[i])
    print(f"{arr[0] // temp}/{arr[i]//temp}")