import sys

S = list(sys.stdin.readline().rstrip())
N = len(S)
char_info = {'0':0, '1':0}
curr_char = S[0]
char_info[curr_char] += 1

for i in range(N):
    if S[i] != curr_char:
        curr_char = S[i]
        char_info[curr_char] += 1
    
print(min(char_info.values()))