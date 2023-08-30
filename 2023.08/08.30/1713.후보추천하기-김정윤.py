import sys

N = int(sys.stdin.readline())
recom = int(sys.stdin.readline())

recom_list = list(map(int, sys.stdin.readline().split()))
recom_cntlist = [0] * 101
q = []

for i in recom_list:
    idx = 1000
    min = 1001
    if len(q) < N:
        if i in q:
            recom_cntlist[i] += 1
        else:
            q.append(i)
    else:
        if i in q:
            recom_cntlist[i] += 1
        else:
            for j in range(len(q)):
                if recom_cntlist[q[j]] < min:
                    idx = j
                    min = recom_cntlist[q[j]]
            recom_cntlist[q[idx]] = 0
            q.pop(idx)
            q.append(i)
        
q.sort()

print(*q)