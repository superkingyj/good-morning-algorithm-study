import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
K = int(sys.stdin.readline())

max_cnt = 0

for row1 in range(N):
    zero_cnt = 0
    
    for num in arr[row1]:
        if num == '0':
            zero_cnt += 1
        
    # 이 행과 똑같은 값을 가진 행의 개수 세기
    row2_cnt = 0
    # 0의 개수가 K보다 작거나 같고
    # 0의 개수가 홀수일땐 K도 홀수, 짝수일땐 K도 짝수여야 함 이 행을 다 켰수 있음
    if zero_cnt <= K and zero_cnt%2 == K%2: 
        
        for row2 in range(N): 
            if arr[row1] == arr[row2]:  # 두 개의 행이 같으면
                row2_cnt += 1
                
    max_cnt = max(max_cnt, row2_cnt) 
    
print(max_cnt)