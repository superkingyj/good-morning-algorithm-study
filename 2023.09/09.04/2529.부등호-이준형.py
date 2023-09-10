from sys import stdin
input= stdin.readline

n = int(input()) # 부등호의 개수
signs = input().rstrip().split() # 부등호 배열
visited = [0]*10 # q방문
res = [] 

def check(x,y,sign):
    return eval(f"{x}{sign}{y}")

def dfs(num, tmp):
    if num == n+1:
        res.append(tmp)
        return
    
    for i in range(10):
        if not visited[i]:
            if num == 0 or check(tmp[-1], i, signs[num-1]):
                visited[i] = 1
                dfs(num+1, tmp+str(i))
                visited[i] = 0

dfs(0,"")

print(res[-1])
print(res[0])


