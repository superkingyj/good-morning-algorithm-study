import sys

while True:
   N, M = map(int,sys.stdin.readline().split())
   if N == 0 and M == 0:
      break
   dic = {}
   count = 0
   for _ in range(N):
      cd = int(sys.stdin.readline())
      dic[cd] = 1

   for _ in range(M):
      cd = int(sys.stdin.readline())
      if cd in dic:
         count += 1

   print(count)