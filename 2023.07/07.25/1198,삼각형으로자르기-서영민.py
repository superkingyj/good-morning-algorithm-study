N = int(input())

dots = [list(map(int, input().split())) for _ in range(N)]


result = 0

for i in range(N):
    for k in range(i+1, N):
        for j in range(k+1, N):
            x1 = dots[i][0]
            y1 = dots[i][1]
            x2 = dots[1][0]
            y2 = dots[1][1]
            x3 = dots[2][0]
            y3 = dots[2][1]
            
            a = x1*y2 + x2*y3 + x3*y1
            b = x2*y1 + x3*y2 + x1*y3
            
            trangle_area = 0.5*(abs(a-b))
            
            if result < trangle_area:
                result = trangle_area
                
print(result) 