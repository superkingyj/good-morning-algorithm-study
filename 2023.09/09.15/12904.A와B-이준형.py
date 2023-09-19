S = list(input())
T = list(input())

while len(S)!=len(T):
    if T[-1] == 'A':
        T.pop()
    else:
        T = T[::-1]
        T.pop(0)

if S==T :
    print(1)
else:
    print(0)