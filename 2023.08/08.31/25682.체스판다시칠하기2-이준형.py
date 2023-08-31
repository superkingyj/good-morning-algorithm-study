import sys
input = sys.stdin.readline

n,m,k = list(map(int,input().rstrip().split()))

b=[[0]*(m+1) for j in range(n+1)]
w=[[0]*(m+1) for j in range(n+1)]

for i in range(1,n+1):
    a= list(input().rstrip())
    for j in range(1,m+1):
        w[i][j]=w[i-1][j]+w[i][j-1]-w[i-1][j-1]
        b[i][j]=b[i-1][j]+b[i][j-1]-b[i-1][j-1]
        if (j+i)%2==0:
            if a[j-1]=="B":
                w[i][j]+=1
            else:
                b[i][j]+=1
        else:
            if a[j-1]=="W":
                w[i][j]+=1
            else:
                b[i][j]+=1
minres = 4000000
for r in range(k,n+1):
    for s in range(k,m+1):
        minres = min(minres,w[r][s]-w[r-k][s]-w[r][s-k]+w[r-k][s-k],b[r][s]-b[r-k][s]-b[r][s-k]+b[r-k][s-k])
        
print(minres)