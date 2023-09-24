# 슬라이딩 윈도우??
# 문제의도는 파악했으나 코드를 이해를 못하겠습니다..
# 도와주세요...

# import sys

# s = sys.stdin.readline()
# n = len(s)
# acount = s.count('a')
# m = 99999999


# for i in range(n) :
#     bcnt = 0    # bcnt의미는?
#     plus = 1    # plus의미는?
#     while plus <= acount :
#         if s[(i+plus)%n]=='b': # 왜 n으로 나누는걸까?
#             bcnt += 1
#         plus += 1
#     m = min(bcnt, m)

# print(m)

# ==========================================

# 슬라이딩 개념이 들어간 부분은????
import sys

string = sys.stdin.readline().rstrip()
a_cnt = string.count("a")
result = sys.maxsize

for i in range(len(string)):
    tmp_string = ""
    for j in range(i, i+a_cnt):
        tmp_string += string[j%len(string)] # 초과된 index를 위해서 len모듈러를 해준거다 (원형으로 연산을 해주기 위해서)
    
    b_cnt = tmp_string.count("b")
    result = min(b_cnt, result)

print(result)