# # 시간초과 에러
# # 이중for문으로 O(n2)

# import sys
# input = sys.stdin.readline

# n = int(input())
# li = list(map(int, input().split()))

# ans = [0]*n

# for i in range(n) :
#     for j in range(i,n) :
#         if li[i] < li[j] :
#             ans[i] = li[j]
#             break
#         else :
#             ans[i] = -1

# print(*ans)

# 스택으로 풀기
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
stack = []
ans = [-1] * n

for i in range(n) :
    while stack and li[stack[-1]] < li[i] :
        ans[stack.pop()] = li[i]
    stack.append(i)

print(*ans)
