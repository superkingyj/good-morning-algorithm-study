
x = int(input())

line = list(input())

woman = 0
man = 0

for i in range(len(line)):
    if abs(man-woman) < x:
        if line[i] == 'M':
            man += 1
        else:
            woman += 1
    else:
        if line[i] == 'M':
            if man < woman:
                man += 1
            else:
                if i+1 < len(line) and line[i+1] == 'W':
                    line[i], line[i+1] = line[i+1], line[i]
                    woman += 1
                else:
                    break
        else:
            if man > woman:
                woman += 1
            else:
                if i+1 < len(line) and line[i+1] == 'M':
                    line[i], line[i+1] = line[i+1], line[i]
                    man += 1
                else:
                    break
                
            


print(woman+man)