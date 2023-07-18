import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = [0] * N

for i in range(N):
    bigger_num_cnt = 0
    for j in range(N):
        # 현재 수보다 큰 수의 개수가 일치하고 해당 자리가 비어있다면
        if bigger_num_cnt == arr[i] and result[j] == 0:
            result[j] = i+1
            break
        # 현재 수보다 큰 수의 개수가 일치하지 않지만 해당 자리가 비어있다면
        elif result[j] == 0:
            bigger_num_cnt += 1

print(*result)     
"""
arr = 2 1 1 0
idx = 1 2 3 4 
rst = 0 0 0 0 

idx rst
1 - 0 0 1 0
2 - 0 2 1 0
3 - 0 2 1 3
4 - 4 2 1 3
"""