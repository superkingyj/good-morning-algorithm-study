import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))


for i in range(1, N):
    # i라인의 0, 1, 2 집에 이전 집들의 현재 집의 번호가 아닌 다른 번호들 추가
    # [1][0] 이면 [0][1] [0][2]을 넣어서 겹치지 않도록
    arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])
    arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
    arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])
    
print(min(arr[-1]))