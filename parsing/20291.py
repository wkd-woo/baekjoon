from collections import defaultdict

N = int(input())
db = defaultdict(int)

for _ in range(N):
    extension = input().split('.')[1]
    db[extension] += 1

keys = sorted(db.keys())
for K in keys:
    print(K, db[K])