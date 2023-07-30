import sys

sys.setrecursionlimit(10**7)
N = int(sys.stdin.readline())
result = 0

def is_multiple_of_3(num):
    return (num % 3) == 0

def dfs(n, cnt, num):
    global result
    
    if cnt == n:
        # print(num)
        if is_multiple_of_3(int("".join(num))):
            result += 1
        return
        
    for i in range(3):
        if cnt == 0 and i == 0: continue
        dfs(n, cnt+1, num + [str(i)])
        
        
dfs(N, 0, [])
print(result)