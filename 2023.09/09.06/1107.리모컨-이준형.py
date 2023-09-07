import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = set(input().split()) if m else set()

if n==100: print(0); exit()

ans = abs(int(n) - 100)

for i in range(1000001):
    if all(digit not in broken for digit in str(i)):
        ans = min(ans, len(str(i)) + abs(int(n-i)))

print(ans)