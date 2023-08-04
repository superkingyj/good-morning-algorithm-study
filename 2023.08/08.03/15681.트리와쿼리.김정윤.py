import sys
sys.setrecursionlimit(10 ** 6)

# count에 해당하는 갯수 저장 예를 들어 5 밑에 4와 6이 있는데, 
# 실행되면 arr[x]로 count[i] for문을 돌려서 count[5]에 1을 저장하고, count[4]에 1을 저장하고
# 그런식으로 가다가 아래부터 4는 몇개를 가지고 있고, 6은 몇개를 가지고 있어서 그 개수를 최종적으로 5에 더하는 구조

def countPoint(x):
    count[x] = 1
    for i in arr[x]:
        if count[i] == 0:
            countPoint(i)
            count[x] += count[i]
        
        
N, R, Q = map(int, sys.stdin.readline().split())

count = [0] * (N + 1)
arr = [[]for _ in range(N + 1)]

for _ in range(N - 1):
    startNode, EndNode = map(int, sys.stdin.readline().split())
    # 어떤 노드와 맞닿아있는지 저장
    arr[startNode].append(EndNode)
    arr[EndNode].append(startNode)
    
# 트리 루트로 먼저 함수 실행
countPoint(R)

for i in range(Q):
    U = int(sys.stdin.readline())
    # 함수를 돌려 찾아놓은 count 배열에서 해당하는 인덱스 번호로 찾음
    print(count[U])
