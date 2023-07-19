#다익스트라
import sys;
import heapq;

inf = sys.maxsize;

#테스트 케이스
T = int(input())

for _ in range(T):
    n, d, c = map(int,input().split())
    #의존성 배열 할당
    array = [[] for _ in range(n)]
    #감염되기까지 걸리는 시간
    dp = [inf for _ in range(n)]
    dp[c-1] = 0
    heap = [[0, c-1]]
    
    #의존관계
    for _ in range(d):
        a, b, s = map(int(input().split()))
        array[b-1].append([a-1,s])
        
    #최소 감염시간 구하기
    while heap:
        curTime, cur = heapq.heappop(heap)
        for  next, nextTime in array[cur]:
            if nextTime < dp[next]:
                dp[next] = nextTime
                heapq.heappush(heap,[nextTime, next])


    cnt = 0
    ans =-1
    for value in dp:
        if value != inf:
            cnt += 1
            ans = max(ans, value)

print(cnt, ans)


