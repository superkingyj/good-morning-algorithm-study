import sys, math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0: return False
    return True

def dfs(cnt, nums):

    if cnt == N:
        print("".join(nums)) # print(233333)
        return
        
    for i in range(1, 10):
        new_num = int("".join(nums) + str(i)) # cnt=0, nums=[2] -> new_num = 29
        if is_prime_number(new_num):
            dfs(cnt+1, nums + [str(i)]) # cnt = 1, nums = ['2', '9']

N = int(sys.stdin.readline())

for num in [2, 3, 5, 7]:
    dfs(1, [str(num)])