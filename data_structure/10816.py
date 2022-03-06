from sys import stdin
from collections import Counter

n = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
target = list(map(int, stdin.readline().split()))

count = Counter(cards)

for i in range(m):
    if cards[i] in count:
        print(count[target[i]], end=' ')
    else:
        print(0, end=' ')
