import sys

N = sys.stdin.readline()

rpms = list(map(int, sys.stdin.readline().split()))

def gcd(x, y):
    
    while y:
        x, y = y, x % y
    return x

for i in range(1, len(rpms)):
    g = gcd(rpms[0], rpms[i])
    print(f'{rpms[0]//g}/{rpms[i]//g}')