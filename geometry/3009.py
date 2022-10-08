from collections import defaultdict


point = []
db_x = defaultdict(int)
db_y = defaultdict(int)
for _ in range(3):
    x, y = map(int, (input().split()))
    db_x[x] += 1
    db_y[y] += 1

result = []
for K, V in db_x.items():
    if V == 1:
        result.append(K)

for K, V in db_y.items():
    if V == 1:
        result.append(K)

print(*result)
