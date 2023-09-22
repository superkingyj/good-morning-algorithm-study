def solve(A,B,C):
    if B == 1:
        return A%C
    else:
        tmp = solve(A, B//2, C)
        if B%2 == 0:
            return tmp*tmp%C
        else:
            return tmp*tmp*A%C

if __name__ == "__main__":
    A,B,C = map(int,input().split())
    print(solve(A,B,C))