#슬라이딩 윈도우
str = input()
#a갯수
a_cnt = str.count('a')
ans = 1001

for i in range(len(str)):
    sub = ''
    if i + a_cnt >= len(str):
        temp = (i + a_cnt) % len(str)
        #0부터 마까지 슬라이딩 윈도우
        sub = str[i:len(str)] + str[0:temp]
    else:
        sub = str[i:i+a_cnt]

    #b갯수
    b_cnt = sub.count('b')
    ans = min(ans, b_cnt)

print(ans)