from collections import deque
from itertools import combinations

while True:
    c = deque(map(int, input().split()))
    k = c.popleft()
    if k == 0:
        break

    for i in combinations(c, 6):
        print(*i)

    print()
