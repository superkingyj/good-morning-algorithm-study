from collections import deque

N, M, V = list(map(int, input().split()))
matrix = [[0]*(N+1) for i in range(N+1)]

v_dfs = [0]*(N+1)
v_bfs = [0]*(N+1)

for i in range(M):
  a,b=map(int,input().split())
  matrix[a][b]=matrix[b][a]=1

def dfs(V):
  v_dfs[V]=1

  for i in range(1, N+1):
    if(v_dfs[i]==0 and matrix[V][i]==1):
      dfs(i)

def bfs(V):

  queue=deque([V])
  v_bfs[V]=1

  while queue:
    V=queue.popleft()
    print(V, end=' ')
    for i in range(1, N+1):
      if(v_bfs[i]==0 and matrix[V][i]==1):
        queue.append(i)
        v_bfs[i]=1

dfs(V)
print()
bfs(V)