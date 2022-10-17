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
    for K, V in sorted(cnt.items(), key=lambda x: (x[1], x[0])):
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
    sentence = input().split()
    case = 1
    for l in sentence:
        cnt = defaultdict(int)
        first, last = l[0], l[-1]
        for each in l[1:-1]:
            cnt[each] += 1

        mid = []
        for K, V in sorted(cnt.items(), key=lambda x: (x[1], x[0])):
            mid.append(''.join([K, str(V)]))
        mid = ''.join(mid)

        if len(l) == 2:
            key = ''.join([first, last])
        elif len(l) == 1:
            key = first
        else:
            key = ''.join([first, mid, last])

        case = case * db[key]

    answer.append(case)

for each in answer:
    print(each)
