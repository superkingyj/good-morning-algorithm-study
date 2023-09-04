import sys

group_count = 0
house_count = 0

n = int(sys.stdin.readline())
houses = []
for _ in range(n):
    houses.append(list(sys.stdin.readline()))


def dfs(houses, i, j, n):
    global house_count

    if i < 0 or i >= n or j < 0 or j >= n or houses[i][j] != "1":
        return

    houses[i][j] = "#"
    house_count += 1

    dfs(houses, i + 1, j, n)
    dfs(houses, i - 1, j, n)
    dfs(houses, i, j + 1, n)
    dfs(houses, i, j - 1, n)


def solve(n, houses):
    global group_count
    global house_count

    house_counts = []

    for i in range(n):
        for j in range(n):
            if houses[i][j] == "1":
                group_count += 1
                dfs(houses, i, j, n)
                house_counts.append(house_count)
                house_count = 0

    print(group_count)
    house_counts.sort()
    [print(house_count) for house_count in house_counts]


solve(n, houses)
