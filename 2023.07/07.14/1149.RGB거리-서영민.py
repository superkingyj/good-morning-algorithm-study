N = int(input())

rgb = [list(map(int, input().split()))]

for i in range(1, N):
    temp = [0, 0, 0]
    red, green, blue = map(int, input().split())
    temp[0] = red + min(rgb[i-1][1], rgb[i-1][2])
    temp[1] = green + min(rgb[i-1][0], rgb[i-1][2])
    temp[2] = blue + min(rgb[i-1][1], rgb[i-1][0])
    rgb.append(temp)
    
print(min(rgb[-1]))