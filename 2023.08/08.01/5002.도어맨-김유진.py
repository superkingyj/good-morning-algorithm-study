import sys

X = int(sys.stdin.readline())
stack =list(sys.stdin.readline().rstrip())
stack.reverse()

w_cnt, m_cnt = 0, 0

while stack:
    curr = stack.pop()
    # 여자이고
    if curr == "W":
        # 입장시켰을 때 차이가 X 이하라면
        if abs((w_cnt+1) - m_cnt) <= X: 
            w_cnt += 1
        # 입장시켰을 때 차이가 X 초과라면
        elif stack:
            next = stack.pop()
            # 만약 남자이고 넣었을 때 차이가 X이하라면
            if next == "M" and abs((m_cnt+1)-w_cnt) <= X:
                m_cnt += 1
                stack.append(curr)
            else: 
                break

    # 남자이고
    else:
        # 입장시켰을 때 차이가 X 이하라면
        if abs((m_cnt+1)-w_cnt) <= X:
            m_cnt += 1
        elif stack:
            next = stack.pop()
            # 만약 여자이고 넣었을 때 차이가 X이하라면
            if next == "W" and abs((w_cnt+1)-m_cnt) <= X:
                w_cnt += 1
                stack.append(curr)
            else: 
                break
            
print(w_cnt+m_cnt)