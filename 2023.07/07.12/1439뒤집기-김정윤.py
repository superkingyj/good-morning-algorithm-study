import sys

S = sys.stdin.readline().rstrip()

# 수가 바뀌는 횟수 저장
cnt = 0

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        cnt += 1
        
# 둘 중 하나만 바꾸면 되기 때문에 2로 나눠줌
# cnt가 홀수 일때를 생각해서 + 1
# ex) 0101 이면 cnt가 3이라서 2로 나누면 1이 되는데, 답은 2이다.
print((cnt + 1) // 2)
