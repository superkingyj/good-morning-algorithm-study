import sys
input = sys.stdin.readline

N = int(input())
entrance = {}

for _ in range(N):
    name, log = input().strip().split(' ')
    entrance[name] = log
    
res = []

for name, log in entrance.items():
    if log == 'enter':
        res.append(name)

res.sort(reverse=True)

print(*res, sep='\n')