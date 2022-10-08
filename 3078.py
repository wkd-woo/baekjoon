from sys import stdin
from collections import deque
from itertools import combinations

input = stdin.readline

n, k = map(int, input().split())
l = [len(input()) for i in range(n)]
name_db = set(l)
l = sorted([(each, i) for i, each in enumerate(l)], key=lambda x: (x[0], x[1]))
l = deque(l)

cnt = 0
for len_ in name_db:
    cand = []
    while l and l[0][0] == len_:
        cand.append(l.popleft())

    for a, b in combinations(cand, 2):
        if abs(a[1] - b[1]) <= k:
            cnt += 1

print(cnt)
