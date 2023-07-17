import sys

string = sys.stdin.readline().rstrip()
a_cnt = string.count("a")
result = sys.maxsize

for i in range(len(string)):
    tmp_string = ""
    for j in range(i, i+a_cnt):
        tmp_string += string[j%len(string)]
    
    b_cnt = tmp_string.count("b")
    result = min(b_cnt, result)

print(result)