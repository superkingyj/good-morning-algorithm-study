# https://www.acmicpc.net/problem/1713
# 문제는 쉬운데 조건이 많아서 어디서부터 조건을 줘야할지 햇갈린다.

n = int(input())
vote = int(input())
li = list(map(int, input().split()))

fram = []
students = {}
for i in range(101) :
    students[i] = 0

for student in li :
    if len(fram) < n :
        fram.append(student)
        # 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
        students[student] += 1
    else :
        # 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
        students[student] += 1
        if student not in fram :
            # 이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 
            # 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.
            min_fram = 1001
            temp = 0
            for picture in fram :
                if min_fram > students[picture] :
                    temp = picture
                    min_fram = students[picture]
            # 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고,
            fram.remove(temp)
            # 그 자리에 새롭게 추천받은 학생의 사진을 게시한다
            fram.append(student)
            # 사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.
            students[temp] = 0
fram.sort()
print(*fram)                