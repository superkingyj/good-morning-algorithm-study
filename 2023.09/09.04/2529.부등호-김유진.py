import sys

K = int(sys.stdin.readline())
sign = list(sys.stdin.readline().rstrip().split())
max_val = ""
min_val = "9999999999"

def is_possible(curr_num, next_num, idx):
    if sign[idx] == "<" and curr_num < next_num: return True
    if sign[idx] == ">" and curr_num > next_num: return True
    return False

def dfs(num_list, cnt):
    global max_val, min_val, visited
    
    if cnt == K+1:
        max_val = max("".join(num_list), max_val)
        min_val = min("".join(num_list), min_val)
        return
    
    for next_num in range(0, 10):
        if not visited[next_num] and is_possible(int(num_list[-1]), next_num, cnt-1):
            visited[next_num] = True
            dfs(num_list + [str(next_num)], cnt+1)
            visited[next_num] = False

for num in range(0, 10):
    visited = [False] * 10
    visited[num] = True
    dfs([str(num)], 1)

print(max_val)
print(min_val)