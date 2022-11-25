n = int(input())
l = list(map(int, input().split()))
db = dict()
for i, each in enumerate(sorted(set(l))):
    if each not in db:
        db[each] = i

result = [db[each] for each in l]
print(*result)
