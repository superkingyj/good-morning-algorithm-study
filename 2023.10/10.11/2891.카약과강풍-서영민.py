import sys
input = sys.stdin.readline

N, S ,R = map(int, input().split())
breakdown = list(map(int, input().split()))
spareteams = list(map(int, input().split()))

teams = [1] * (N+2)
teams[0] = 0
teams[-1] = 0
for i in breakdown:
    teams[i] -= 1

for i in spareteams:
    teams[i] += 1
    
for i in range(1, N+1):
    if teams[i] == 0:
        if teams[i-1] == 2:
            teams[i-1] -= 1
            teams[i] += 1
        elif teams[i+1] == 2:
            teams[i+1] -= 1
            teams[i] += 1

print(teams.count(0) - 2)