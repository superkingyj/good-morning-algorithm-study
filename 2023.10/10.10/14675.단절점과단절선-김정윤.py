import sys
N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
    

q = int(sys.stdin.readline())
for i in range(q):
    t, k = map(int, sys.stdin.readline().split())
    if t == 2:
        print('yes')
    else:
        if len(tree[k]) < 2:
            print('no')
        else:
            print('yes')