# N, M = map(int, input().split())

# tree_length = list(map(int, input().split()))

# start = 1
# end = max(tree_length)

# while start <= end:
#     mid = (start+end)//2
    
#     total = 0
#     for i in range(N):
#         if tree_length[i]>mid:
#             total += tree_length[i]-mid
    
#     if total >= M:
#         start = mid+1
#     else:
#         end = mid-1


# print(end)
N, M = map(int, input().split())

tree_length = list(map(int, input().split()))

start = 1
end = max(tree_length)

def solution(start, end, target, N):
    mid = (start+end)//2
    
    total = 0
    for i in range(N):
        if tree_length[i] > mid:
            total += tree_length[i]-mid
    if total == target:
        return mid
    if total >= M:
        return solution(mid+1, end, target, N)
    else:
        return solution(start, mid-1, target, N)


print(solution(start, end, M, N))