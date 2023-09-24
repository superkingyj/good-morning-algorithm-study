


# #dfs
# #재귀함수
# import sys
# input = sys.stdin.readline

# #갯수 입력
# n = int(input())
# #수열 입력
# num = list(map(int, input().split()))
# #연산자 입력
# add, sub, mul, div = map(int, input().split());

# #최댓값, 최솟값 초기화
# max_result = int(-1e9)
# min_result = int(1e9)


# def dfs(idx, sum, add, sub, mul, div):
#     global max_result, min_result
#     if idx == n:
#         max_result = max(max_result,sum)
#         min_result = min(min_result,sum)
#         return

#     #더하기
#     if add:
#         dfs(idx + 1, sum + num[idx], add - 1, sub, mul, div)
#     #곱하기
#     if sub:
#         dfs(idx + 1, sum - num[idx], add, sub - 1, mul, div)
#     #곱하기
#     if mul:
#         dfs(idx + 1, sum * num[idx], add, sub, mul - 1, div)
#     #빼기
#     if div:
#         dfs(idx + 1, int(sum / num[idx]), add, sub, mul, div - 1)

# #메서드 호출
# dfs(1, num[0], add, sub, mul, div)

# print(max_result)
# print(min_result)