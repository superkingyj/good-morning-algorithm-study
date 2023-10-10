import sys
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
    
q = int(input())

for _ in range(q):
    t, k = map(int, input().split())
    
    if t == 1:
        if len(tree[k]) >= 2:
            print("yes")
        else:
            print("no")
    else:
        print("yes")