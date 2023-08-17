import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input())
rings = list(map(int, input().split()))
    
for i in range(1, n):
    t = gcd(rings[0], rings[i])
    print(f'{rings[0] // t}/{rings[i] // t}')