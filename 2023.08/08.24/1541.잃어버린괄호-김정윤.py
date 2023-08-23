import sys

# -와 +만으로 구성되어 있기 때문에 - 를 먼저 split
str = sys.stdin.readline().rstrip().split('-')
arr = []
sumval = 1e9

for i in range(len(str)):
    temp = 0
    # + 를 기준으로 split
    arr = str[i].split('+')
    
    for j in range(len(arr)):
        temp += int(arr[j])
        
    # 맨 처음 값 추가
    if sumval == 1e9:
        sumval = temp
        
    # temp에 + 연산자로 붙은 것들을 다 합한 뒤 빼줌
    else:
        sumval -= temp
        
print(sumval)