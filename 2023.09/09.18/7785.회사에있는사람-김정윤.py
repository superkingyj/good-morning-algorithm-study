N = int(input())
record = set()

for _ in range(N):
    name, action = input().split()
    if action == 'enter':
        record.add(name)
    else:
        record.remove(name)
        
result = sorted(record, reverse=True)
for i in result:
    print(i)