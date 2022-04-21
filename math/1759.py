from itertools import combinations

l, c = map(int, input().split())
m = list(input().split())
m.sort()
aeiou = set(['a', 'e', 'i', 'o', 'u'])

res = []
for each in combinations(m, l):  # 일단 뽑음
    res.append(each)

for i in res:  # 모음 없는 경우 제거
    if 'a' not in i and 'e' not in i and 'i' not in i and 'o' not in i and 'u' not in i:
        res.remove(i)

for i in res:
    cnt = 0
    for j in i:  # 자음 개수 세서
        if j not in aeiou:
            cnt += 1

    if 1 < cnt != l:  # 자음 개수가 2 이상이면 출력
        print(' '.join(i).replace(' ', ''))
