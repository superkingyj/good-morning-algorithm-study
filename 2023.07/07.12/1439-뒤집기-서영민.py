string = input()

count = 0
for i in range(1, len(string)):
    if string[i-1] != string[i]:
        count += 1
print((count+1)//2)