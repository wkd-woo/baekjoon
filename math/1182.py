from itertools import combinations

n, s = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0
for i in range(1, n + 1):
    for j in combinations(l, i):
        if sum(j) == s:
            cnt += 1

print(cnt)