#레벨-0 버거는 패티만으로 이루어져 있다.
#레벨-L 버거는 햄버거번, 레벨-(L-1) 버거, 패티, 레벨-(L-1)버거, 햄버거번으로 이루어져 있다. (L ≥ 1)
#N과 X가 주어진다
#재귀
#첫 번째는 x값이 중간패티 위치보다 작은 경우
#두 번째는 x값이 중간패티 위치와 같은 경우
#세 번째는 x값이 중간패티 위치보다 크고 전체 재료수보다 작은 경우
#네 번째는 x값이 전체 재료수와 같은 경우

 
def getP( n, x ):
    if n==0:
        if x==0: return 0
        elif x==1: return 1  
    elif x==1:
        return 0
    elif x <= 1+h[n-1]:
        return getP( n-1, x-1 )
    elif x == 1+h[n-1]+1:
        return p[n-1]+1
    elif x <= 1+h[n-1]+1+h[n-1]:
        return p[n-1]+1+getP( n-1, x-(1+h[n-1]+1) )
    else:
        return p[n-1] + 1 + p[n-1]

n, x = map(int, input().split())
#h[n] = 레벨 n의 전체 재료수 = 1 + (레벨 n-1의 전체재료수) + 1 + (레벨 n-1의 전체재료수) + 1
h = [1] * (n+1)
#p[n] = 레벨 n의 패티수 = (레벨 n-1의 패티수) + 1 + (레벨 n-1의 패티수)
p = [1] * (n+1)

for i in range( 1, n+1 ):
    h[i] = 1 + h[i-1] + 1 + h[i-1] + 1
    p[i] = p[i-1] + 1 + p[i-1]

print( getP( n, x ) )