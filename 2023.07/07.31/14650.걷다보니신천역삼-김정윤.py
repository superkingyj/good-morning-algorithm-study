import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
count = 0

def check(n, sum):
    global count
    for i in range(3):
        if n == 0 and i == 0:
            continue
        if n == N:
            if sum % 3 == 0:
                count += 1
                return count
        else:
            check(n + 1, int(str(sum + i)))
            
check(0, 0)
print(count)