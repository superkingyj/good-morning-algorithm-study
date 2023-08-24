import sys

arr = sys.stdin.readline().rstrip().split("-")
result = 0

for num in arr[0].split("+"):
    result += int(num)

for string in arr[1:]:
    for num in string.split("+"):
        result -= int(num)

print(result)