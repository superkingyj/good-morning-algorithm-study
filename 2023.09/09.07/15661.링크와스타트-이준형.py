from sys import stdin
input = stdin.readline
def calc(team):
    ability = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if i != j:
                ability += graph[team[i]][team[j]]
    return ability

def dfs(idx, team1, team2):
    global ans

    if idx == n:
        if len(team1) > 0 and len(team2) > 0:
            ability1 = calc(team1)
            ability2 = calc(team2)
            ans = min(ans, abs(ability1 - ability2))
        return

    dfs(idx + 1, team1 + [idx], team2)
    dfs(idx + 1, team1, team2 + [idx])

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')
dfs(0, [], [])

print(ans)