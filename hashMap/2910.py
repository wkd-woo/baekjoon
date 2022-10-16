from collections import defaultdict

n, c = map(int, input().split())
l = list(map(int, input().split()))
db = defaultdict(int)
for each in l:
    db[each] += 1


result = [[K] * V for K, V in sorted(db.items(), key=lambda x:-x[1])]
result = sum(result, [])
print(*result)
