import random

# 참여자 입력
peoples = ['채홍', '성원', '유진', '영민', '정윤']

# 날짜 입력
start_date = 12
end_date = 14

presenters = random.sample(peoples, end_date-start_date+1)
for date, presenter in zip(range(start_date, end_date+1), presenters):
    print(f"{date}일: {presenter}")