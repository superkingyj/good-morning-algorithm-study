import sys
# recursionerror 때문에 추가한 최대 재귀 깊이 변경 코드
sys.setrecursionlimit(10**5)

def dfs(node, weight):
    for n, l in tree[node]:
        cost = weight + l
        # 방문하지 않은 곳일 때
        if visited_dfs[n] == -1:
            # 해당 노드까지 가는 비용 추가
            visited_dfs[n] = cost
            dfs(n, cost)
    return

N = int(sys.stdin.readline())

#방문하지 않은 곳은 -1로 초기화

tree = [[] * N for _ in range(N + 1)]

# tree에 담았을 때의 구조. child_node와 line을 0~12까지 담은 상태
for i in range(N - 1):
    parent_node, child_node, line = map(int, sys.stdin.readline().split())
    tree[parent_node].append((child_node, line))
    tree[child_node].append((parent_node, line))

# 첫 번째 노드로 dfs 탐색
visited_dfs = [-1] * (N + 1)
visited_dfs[1] = 0
dfs(1, 0)

# visited_dfs = [0, . ,.,..] 으로 1부터 12번 노드까지 각각 간선의 가중치들이 담겨있음
# 가장 가중치가 높은 값을 idx에 저장
idx = visited_dfs.index(max(visited_dfs))

# 방문 초기화     
visited_dfs = [-1] * (N + 1)

# 처음 노드(가중치가 가장 높은)를 0으로 초기화
visited_dfs[idx] = 0
# 해당 노드에서 시작해서 가중치 계산해서 visited_dfs에 추가
dfs(idx, 0)

# 가장 높은 값 출력
print(max(visited_dfs))