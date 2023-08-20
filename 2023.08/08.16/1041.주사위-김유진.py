import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

if N == 1:
    arr.sort()
    print(sum(arr) - max(arr))
else:
    one_cnt = (N-2)*(N-2) + 4*(N-1)*(N-2)
    two_cnt = 4*(N-1) + 4*(N-2) 
    three_cnt = 4 # 3면이 보이는 주사위는 무조건 4개
    
    nums = [min(arr[0], arr[5]), min(arr[1], arr[4]), min(arr[2], arr[3])]
    nums.sort()
    
    one_val = nums[0] * one_cnt
    two_val = (nums[0] + nums[1]) * two_cnt
    three_val = (nums[0] + nums[1] + nums[2]) * three_cnt
    
    print(one_val + two_val + three_val)