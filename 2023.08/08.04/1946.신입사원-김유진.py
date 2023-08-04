import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    # 면접 점수 기준 오름차순 정렬
    arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    arr.sort()
    
    # 가장 높은 면접 점수 지원자의 인덱스 저장
    max_docum_idx = 0
    result = 1
    
    for i in range(1, N):
        # 현재 지원자가 이전 지원자들 중 가장 면접 점수 지원자의 면접점수보다 높다면
        if arr[i][1] < arr[max_docum_idx][1]:
            result += 1
            max_docum_idx = i
    
    print(result)