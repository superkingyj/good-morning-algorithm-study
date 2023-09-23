n = int(input())
tmp = input().lower().rstrip()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for c in alphabet:
    tmp = tmp.replace(c, ' ')

tmp = list(map(int, tmp.split()))

print(sum(tmp))