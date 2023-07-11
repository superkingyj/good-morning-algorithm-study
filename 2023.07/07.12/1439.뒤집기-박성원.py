S = input()
count = 0

# 숫자가 바뀐 횟수와 뒤집은 횟수에서 관계발견

for i in range(1, len(S)) :
    if S[i] != S[i-1] :
        count+=1

print((count+1)//2)