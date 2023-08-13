import sys

input_ = sys.stdin.readline

n, m = map(int, input_().split())

visited = [0]*(n)
temp = []
result = set()

numbers = list(map(int, input_().split()))
numbers.sort()

def dfs(depth):
    prev = 0
    if depth == m:
        result.add(tuple(temp))
        return
    for i in range(n):
        if numbers[i] != prev and not visited[i]:
            prev = numbers[i]
            visited[i] = 1
            temp.append(numbers[i])
            dfs(depth+1)
            temp.pop()
            visited[i] = 0

dfs(0)

for i in list(result):
    print(*i)