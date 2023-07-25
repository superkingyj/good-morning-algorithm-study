import sys
input = sys.stdin.readline

# 숫자판 만들기
board = [list(map(str, input().split())) for _ in range(5)]
result = []

# 6자리 문자열을 만들어야하기 때문에 재귀함수 이용
def dfs(x, y, number):
    if len(number) == 6: #6자리 숫자가 만들어졌다면
        if number not in result: #result에 없다면
            result.append(number)
        return
        
    dx = [1, -1, 0, 0] #상하좌우 확인 x
    dy = [0, 0, 1, -1] #상하좌우 확인 y
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]
        
        if 0 <= ddx < 5 and 0 <= ddy < 5: #범위 내에 있다면
            dfs(ddx, ddy, number + board[ddx][ddy]) #6글자가 될 때 까지 재귀

# 모든
for i in range(5) :
    for j in range(5) :
        dfs(i, j, board[i][j])


print(len(result))

