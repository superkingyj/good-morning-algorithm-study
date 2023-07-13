import random

# 참여자 입력
peoples = ['채홍', '성원', '유진', '영민', '정윤']

# 날짜 입력
start_date = 12
end_date = 14

for date in range(start_date, end_date+1):
    print(f"{date}일: {random.choice(peoples)}")