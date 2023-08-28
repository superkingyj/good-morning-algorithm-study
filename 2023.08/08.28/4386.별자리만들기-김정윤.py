import math
import sys

# 원소 x가 속한 부모 집합의 루트 노드를 찾는 함수
def find_parent(parent, x):
#parent 배열은 각 원소의 부모 노드를 나타내는 배열로 초기에는 자기 자신을 가리키도록 설정
    if parent[x] != x:
# 함수는 재귀적으로 호출되며, 원소 x 의 부모가 자기 자신이 아니라면 부모의 부모를 찾는 과정 반복
        parent[x] = find_parent(parent, parent[x])
        # 원소 x의 부모를 찾아 반환
    return parent[x]

# 두개 원소 a, b를 입력으로 받아 하나의 집합으로 합치는 함수
def union_parent(parent, a, b):
    # find_parent로 부모 노드를 찾음
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 부모 노드가 다르다면 두 집합을 합치기 위해 한 집합의 부모를 다른 집합의 부모로 변경
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 거리 구하는 함수(가중치 or 비용)
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def kruskal(edges, n):
    # 부모 자기 자신으로 초기화
    parent = [i for i in range(n)]
    # edges를 비용 순으로 정렬
    edges.sort(key=lambda x: x[2])
    mst_cost = 0

    for edge in edges:
        a, b, cost = edge
        # 사이클이 발생하지 않는 경우만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            mst_cost += cost

    return mst_cost

n = int(sys.stdin.readline())
stars = []
edges = []

for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

for i in range(n):
    for j in range(i+1, n):
        # 거리 계산
        cost = distance(stars[i], stars[j])
        edges.append((i, j, cost))

result = kruskal(edges, n)
print('{:.2f}'.format(result))
