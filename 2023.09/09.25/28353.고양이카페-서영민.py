N, K = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort()

start, end = 0, len(weight) - 1
count = 0

while start < end:
    if weight[start] + weight[end] <= K:
        count += 1
        start += 1
        end -= 1
    else:
        end -= 1

print(count)