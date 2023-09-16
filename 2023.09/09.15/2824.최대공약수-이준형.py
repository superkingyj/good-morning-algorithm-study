from sys import stdin
input = stdin.readline

def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

N = int(input())
A = eval(input().replace(" ","*"))
M = int(input())
B = eval(input().replace(" ","*"))

print(str(gcd(A,B))[-9:])


