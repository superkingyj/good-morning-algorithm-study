
N = int(input())


def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

result = []
def backtracking(depth, rs):
    
    if depth == N:
        result.append(rs)
        return
    
    for i in range(10):
        temp = rs+str(i)
        number = int(temp)
        if isPrime(number):
            backtracking(depth+1, temp)
            
backtracking(0, "")
for i in result:
    print(i)