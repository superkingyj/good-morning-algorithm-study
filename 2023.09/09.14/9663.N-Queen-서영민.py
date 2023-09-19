N = int(input())

visited = [0] * N
row = [0] * N
res = 0

def nqueen(depth):
    global res
    
    if depth == N:
        res += 1
        return
    
    for i in range(N):
        if not visited[i]:
            row[depth] = i
            if check(depth):
                visited[i] = 1
                nqueen(depth+1)
                visited[i] = 0
def check(n):
    
    for i in range(n):
        if row[i] == row[n] or n-i == abs(row[n] - row[i]):
            return False
    return True
        
nqueen(0)
print(res)