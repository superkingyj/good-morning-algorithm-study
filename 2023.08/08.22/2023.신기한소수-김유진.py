import sys, math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0: return False
    return True

def dfs(cnt, nums):

    if cnt == N:
        print("".join(nums))
        
    for i in range(1, 10):
        new_num = int("".join(nums) + str(i))
        if is_prime_number(new_num):
            dfs(cnt+1, nums + [str(i)])

N = int(sys.stdin.readline())

for num in [2, 3, 5, 7]:
    dfs(1, [str(num)])