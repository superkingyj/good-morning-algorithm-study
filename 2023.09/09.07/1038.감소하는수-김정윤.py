def add_digit(digit,num):    #자리수에 따라 증가
    if digit==1:
        decreasing.append(num)
    else:
        for i in range(num%10):
            add_digit(digit-1,num*10+i)

def backtracking(digit):    #백트래킹 시작
    for i in range(digit-1,10):
        add_digit(digit,i)
    
decreasing=[]        #감소하는 숫자 리스트
for i in range(1,11):
    backtracking(i)

n=int(input())
if n>=len(decreasing):        #감소하는 숫자가 없을 때
    print(-1)
else:
    print(decreasing)