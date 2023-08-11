import sys

N = int(sys.stdin.readline())
arr = []
count = 0

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

while (True):
    if arr[0] == max(arr) and arr.count(max(arr)) == 1:
        break

    # arr 리스트에서 최대값을 찾는데 범위는 1부터 N - 1까지
    i = arr.index(max(arr), 1, N)
    arr[i] -= 1
    arr[0] += 1
    count += 1

print(count)