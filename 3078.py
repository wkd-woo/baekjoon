from sys import stdin
from collections import deque, defaultdict
from itertools import combinations

input = stdin.readline

n, k = map(int, input().split())
l = [len(input()) for _ in range(n)]
db = defaultdict(list)

for i, length in enumerate(l):
    db[length].append(i+1)

answer = 0
for K, V in db.items():
    q = deque(V)
    now = q.popleft()
    temp = []
    while q:
        print(q, temp)
        next_ = q.popleft()
        temp.append(next_)
        if abs(next_ - now) <= K:
            answer += 1
        else:
            q.extendleft(temp)
            now = q.popleft()
            temp = []


print(answer)
