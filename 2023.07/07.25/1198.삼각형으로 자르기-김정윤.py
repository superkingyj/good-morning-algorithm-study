import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split()))) 
    
result = 0

# 이전 좌표보다 크게 하기 위해 i + 1, j + 1부터 시작

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            # 사선(신발끈) 공식 사용해서 가장 큰 값 찾음
            result = max(result, abs((arr[i][0] * arr[j][1] + arr[j][0] * arr[k][1] + arr[k][0] * arr[i][1])
                                    -(arr[j][0] * arr[i][1] + arr[k][0] * arr[j][1] + arr[i][0] * arr[k][1])))
            
            
print(result / 2)