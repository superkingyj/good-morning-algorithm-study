import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
delete_num = int(sys.stdin.readline())

def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)
count = 0

dfs(delete_num, arr)

for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
        
print(count)
