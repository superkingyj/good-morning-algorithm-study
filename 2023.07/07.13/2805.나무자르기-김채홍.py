N, M = map(int(input().split()))
tree = list(map(int(input().split())))
start, end = 1, max(tree)

#start와 end가 같아질 때 까지 반복
while start <= end :
    mid = (start+end) // 2
    sum  = 0 

    for i in tree:
        if i >= mid:
            #절단기보다 크면 자른다
            sum += i - mid
    
    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)