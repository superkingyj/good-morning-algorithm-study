import sys
import re

N = int(sys.stdin.readline())
input_str = sys.stdin.readline()

numbers = list(re.sub(r'[^0-9]', ' ', input_str).split())
print(sum(map(int, numbers)))

