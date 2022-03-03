from collections import deque

n = int(input())
cards = deque([i for i in range(1, n + 1)])
last = 0

while cards:
    if len(cards) == 1:
        last = cards.pop()
    else:
        cards.popleft()
        cards.rotate(-1)

print(last)