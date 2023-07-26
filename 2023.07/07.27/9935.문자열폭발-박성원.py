string = input()
bomb = input()

stack = []

for char in string :
    stack.append(char)
    if char == stack[-1] and ''.join(stack[-len(bomb):]) == bomb :
        del stack[-len(bomb):]

ans = ''.join(stack)

print(ans if ans != "" else "FRULA")

# 문제 해석
# 주어진 단어에 폭발단어가 들어온다면 그 폭발 단어를 빼고 문자열을 이어나가며 폭발물을 제거한다.
# stack을 이용하여 풀이