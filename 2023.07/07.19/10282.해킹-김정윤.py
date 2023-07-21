import sys
import heapq


T = int(sys.stdin.readline())

for i in range(T):
    # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
    n, d, c = map(int, sys.stdin.readline().split())
    
    # arr에 의존 관계 저장
    arr = [[] for _ in range(n + 1)]
    # 감염되기까지 걸리는 시간 저장
    temp = [sys.maxsize] * (n + 1)
    temp[c] = 0
    # queue에는 시작점 추가
    queue = [[0, c]]
    
    for j in range(d):
        # a는 b를 의존, s초 후 a도 감염
        a, b, s = map(int, sys.stdin.readline().split())
        arr[b].append([a, s])
    
    while queue:
        y, z = heapq.heappop(queue)
        for e, v in arr[z]:
            # temp에 최소로 걸리는 시간 찾음
            if temp[e] > y + v:
                temp[e] = y + v
                heapq.heappush(queue, [y + v, e])
                
                
    maxnum = 0
    cnt = 0
    
    for z in temp:
        if z != sys.maxsize:
            maxnum = max(z, maxnum)
            cnt += 1
            
    print(cnt, maxnum)
    
    



