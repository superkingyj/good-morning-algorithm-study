import heapq

n, m = map(int, input().split())

cards = list(map(int, input().split()))

heapq.heapify(cards)

for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    sum_ = x+y
    heapq.heappush(cards, sum_)
    heapq.heappush(cards, sum_)
    
print(sum(cards))