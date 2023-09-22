import sys

def dfs(rn, gold):
    global ans, visited
    if ans == 1:
        return
    
    if arr[rn][0] == 'L':
        if arr[rn][1] > gold:
            gold = arr[rn][1]
    
    elif arr[rn][0] == 'T':
        if arr[rn][1] > gold:
            return
        else:
            gold -= arr[rn][1]
    if rn == n - 1:
        ans = 1
        return;

    visited[rn] = True
    for i in arr[rn][2]:
        if visited[int(i) - 1] == False:
            dfs(int(i) - 1, gold)
    visited[rn] = False

while True:
    n = int(sys.stdin.readline())
    arr = []
    visited = [False] * n
    ans = 0
    if n == 0:
        break
    money = 0
    
    for i in range(n):
        str = sys.stdin.readline().rstrip().split()
        arr.append([str[0], int(str[1]), str[2:]])
    
    dfs(0, 0)
    
    if ans == 0:
        print('No')
    else:
        print('Yes')