import sys

N, M = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(li)

while start<= end :
    middle = (start+end)//2
    lan = 0

    for i in li :
        if i > middle :
            lan += i - middle
        
        if lan < M :
            end = middle - 1
        else :
            start = middle + 1


print(lan)
