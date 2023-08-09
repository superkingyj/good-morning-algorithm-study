import sys

input_ = sys.stdin.readline

n, m = map(int, input_().split())
numbers = list(map(int, input_().split()))

numbers.sort()

visited = [0]*n
result = []
prev = 0

def dfs(depth):
    prev = 0
    if depth == m:
        print(*result)
        return
    for i in range(n):
        if numbers[i] != prev and not visited[i]:
            prev = numbers[i]
            visited[i] = 1
            result.append(numbers[i])
            dfs(depth+1)
            result.pop()
            visited[i] = 0

dfs(0)

