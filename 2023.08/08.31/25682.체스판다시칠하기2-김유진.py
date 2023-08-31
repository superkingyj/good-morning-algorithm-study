import sys
from pprint import pprint

N, M, K = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]


def get_min_val(color):
    prefix = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(M):
            if (i + j) % 2 == 0:
                value = grid[i][j] != color
            else:
                value = grid[i][j] == color
            prefix[i + 1][j + 1] = (
                prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + value
            )

    min_val = sys.maxsize
    for i in range(1, N + 1 - K + 1):
        for j in range(1, M + 1 - K + 1):
            val = (
                prefix[i + K - 1][j + K - 1]
                - prefix[i - 1][j + K - 1]
                - prefix[i + K - 1][j - 1]
                + prefix[i - 1][j - 1]
            )
            min_val = min(min_val, val)

    return min_val


b_val = get_min_val("B")
w_val = get_min_val("W")
print(min(b_val, w_val))
