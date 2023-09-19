import sys

n = int(sys.stdin.readline())

ans = 0
row = [0] * n

# 퀸을 해당 위치에 놓을 수 있는지 확인, 같은 행, 열이랑 다른 대각선에 다른 퀸이 있는 경우
def is_promising(x):
    for i in range(x):              #해당부분은 대각선 확인
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                # 현재 퀸을 놓을 수 있다면 다음 퀸 놓기 위한 것 호출
                n_queens(x + 1)

n_queens(0)
print(ans)