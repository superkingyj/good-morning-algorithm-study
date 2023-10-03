import sys

# 최소 공통 조상
# 1. graph 리스트에 각각 부모를 기록, x와 y 입력
# 2. parent함수 : 자기 자신으로부터 거슬러 올라가 깊이가 0인 부모까지 기록한 리스트 반환
#  -> x, y에 대해서 각각 진행
# 3. 깊이 맞춰주기 (i와 j는 각각 A_parent와 B_parent의 시작 인덱스)
# -> 두 깊이가 같아지도록 index값 조정
# 4. 최소 공통 조상 찾기
# -> 두 부모의 값이 같아질 때까지 탐색
# 5. 출력

def parent(p, x):
    result = [x]
    while p[x]:
        result.append(p[x])
        x = p[x]
    return result


T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    graph = [0] * (N + 1)
    for j in range(N - 1):
        A, B = map(int, sys.stdin.readline().split())
        graph[B] = A
    find_A, find_B = map(int, sys.stdin.readline().split())
    A_parent = parent(graph, find_A)
    B_parent = parent(graph, find_B)
    
    i, j = 0, 0
    if len(A_parent) > len(B_parent):
        i = len(A_parent) - len(B_parent)
        
    else:
        j = len(B_parent) - len(A_parent)
        
    while A_parent[i] != B_parent[j]:
        i += 1
        j += 1
    print(A_parent[i])