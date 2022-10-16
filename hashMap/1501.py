from collections import defaultdict


db = defaultdict(int)
n = int(input())
for _ in range(n):
    l = list(input())
    cnt = defaultdict(int)
    first, last = l[0], l[-1]
    for each in l[1:-1]:
        cnt[each] += 1

    mid = []
    for K, V in sorted(cnt.items(), key=lambda x: x[1]):
        mid.append(''.join([K, str(V)]))
    mid = ''.join(mid)

    if len(l) == 2:
        key = ''.join([first, last])
    elif len(l) == 1:
        key = first
    else:
        key = ''.join([first, mid, last])
    db[key] += 1

answer = []
m = int(input())
for _ in range(m):
    l = list(input())
    cnt = defaultdict(int)
    first, last = l[0], l[-1]
    for each in l[1:-1]:
        cnt[each] += 1

    mid = []
    for K, V in sorted(cnt.items(), key=lambda x: x[1]):
        mid.append(''.join([K, str(V)]))
    mid = ''.join(mid)

    if len(l) == 2:
        key = ''.join([first, last])
    elif len(l) == 1:
        key = first
    else:
        key = ''.join([first, mid, last])

    if key in db:
        answer.append(db[key])
    else:
        answer.append(0)

for each in answer:
    print(each)
