import sys

N = int(sys.stdin.readline())
result = 0
row = [0] * N

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def backtracking(i):
    global result
    if i == N:
        result += 1
        return

    for j in range(N):
        # [i, j]에 퀸을 놓겠다.
        row[i] = j
        if is_promising(i):
            backtracking(i+1)

backtracking(0)
print(result)