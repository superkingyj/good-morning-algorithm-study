N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visit = [False] * N
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(idx, N):
        if not visit[i] and overlap != L[i]:
            out.append(L[i])
            visit[i] = True
            overlap = L[i]
            solve(depth+1, i+1, N, M)
            out.pop()
            visit[i] = False

solve(0, 0, N, M)