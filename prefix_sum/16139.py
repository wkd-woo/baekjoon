from sys import stdin

input = stdin.readline


s = input()
q = int(input())
db = dict()
for each in set(s):  # O(s) = O(200,000)
    db[each] = [0 for _ in range(len(s))]
db[s[0]][0] += 1

for i, each in enumerate(s):  # O(s)
    if i == 0:
        continue
    for K in db.keys():  # a to z max 26
        db[K][i] = db[K][i-1]  # => 26 * 200,000 = 5.2 mio

    db[each][i] += 1

for _ in range(q):  # O(q) = O(200,000)
    a, l, r = input().split()
    l, r = int(l), int(r)
    if l == 0:
        print(db[a][r]) if a in db else print(0)
    else:
        print(db[a][r] - db[a][l-1]) if a in db else print(0)
