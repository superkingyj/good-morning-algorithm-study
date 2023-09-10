import sys
from itertools import combinations

N = int(sys.stdin.readline())
nums = []

for i in range(1, 11):
    for combi in combinations(range(0, 10), i):
        tmp  = list(combi)
        tmp.sort(reverse=True)
        nums.append(int("".join(map(str, tmp))))

nums.sort()

try:
    print(nums[N])
except:
    print(-1)
