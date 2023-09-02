import sys

def 전위(노드,결과):
    결과 += 노드
    for i in tree[노드]:
        if i == ".":
            continue
        결과 = 전위(i,결과)
    return 결과

def 중위(노드,결과):
    if 노드 == ".":
        return 결과
    왼쪽노드,오른쪽노드 = tree[노드]
    결과 = 중위(왼쪽노드,결과)
    결과 += 노드
    결과 = 중위(오른쪽노드,결과)
    return 결과

def 후위(노드,결과):
    if tree[노드] == (".","."):
        return 결과 + 노드
    
    for i in tree[노드]:
        if i == ".":
            continue
        결과 = 후위(i,결과)
    return 결과 + 노드

n = int(sys.stdin.readline())
tree = dict()
for _ in range(n):
    노드,왼쪽노드,오른쪽노드 = sys.stdin.readline().rstrip().split()
    tree[노드] = (왼쪽노드,오른쪽노드)
print(전위("A",""))
print(중위("A",""))
print(후위("A",""))