from itertools import combinations

n, m = map(int, input().split())
l = [i for i in range(1, n + 1)]

for i in combinations(l, m):
    print(*i)