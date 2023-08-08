import sys


N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

def pick_cards():
    cards.sort()
    return cards[0], cards[1]
    
def overwrite(num):
    cards[0], cards[1] = num, num

for _ in range(M):
    x, y = pick_cards()
    overwrite(x+y)
    
print(sum(cards))