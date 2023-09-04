import sys

N = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().rstrip().split())

visited = [False] * 10

max_ans, min_ans = "", ""

def possible(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j

def solve(cnt, s):
    global max_ans, min_ans
    if cnt == N + 1:
        if not len(min_ans):
            min_ans = s
        else:
            max_ans = s
            
        return
    
    for i in range(10):
        if not visited[i]:
            if cnt == 0 or possible(s[-1], str(i), arr[cnt - 1]):
                visited[i] = True
                solve(cnt + 1, s + str(i))
                visited[i] = False
                
solve(0, "")
print(max_ans)
print(min_ans)