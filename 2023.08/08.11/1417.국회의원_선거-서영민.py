import math

n = int(input())

max_num = int(input())
spare = 0
count = 0

for i in range(n-1):
    next = int(input())
    if max_num < next:
        temp = math.ceil((next-max_num)/2) + 1
        max_num += temp
        if spare > 0:
            count += temp - spare
            spare = 0
        else:
            count += temp
            spare = 1
    
print(count)
        