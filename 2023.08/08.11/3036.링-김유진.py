import sys
from fractions import Fraction

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    answer = Fraction(arr[0], 1) / Fraction(arr[i], 1)
    print(answer.numerator, "/", answer.denominator, sep = "")
