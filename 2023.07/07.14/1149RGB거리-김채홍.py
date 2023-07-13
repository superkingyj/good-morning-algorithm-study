n = int(input())
rgbdp = []  #최소값

for i in range(n):
    rgbdp[i] = list(map(int,input().split()))
    
for i in range(1,n): 
    #1번집
    rgbdp[i][0]= min(rgbdp[i-1][1],rgbdp[i-1][2]) + rgbdp[i][0] #전값 전전값
    #2번집
    rgbdp[i][1]= min(rgbdp[i-1][0],rgbdp[i-1][2]) + rgbdp[i][1] #겹치지않게
    #3번집
    rgbdp[i][2]= min(rgbdp[i-1][0],rgbdp[i-1][1]) + rgbdp[i][2]

print(min(rgbdp[n-1][0],rgbdp[n-1][1],rgbdp[n-1][2]))