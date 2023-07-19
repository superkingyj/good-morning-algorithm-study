import sys

str = sys.stdin.readline().rstrip()

a_count = str.count('a')

# 원형 문자열이기 때문에 문자열 늘려줌
str += str[0: a_count - 1]

minvalue = 1000000000000000

# 기존 입력된 문자열의 길이가 변형되었기 때문에 빼줌
for i in range(len(str) - (a_count - 1)):
    # 슬라이싱한 문자열 내부의 b의 개수를 구해서 최솟값 찾음
    minvalue = min(minvalue, str[i: i + a_count].count('b'))
    
print(minvalue)
    