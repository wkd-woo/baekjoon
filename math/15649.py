from itertools import permutations

n, m = map(int, input().split())

l = [i for i in range(1, n + 1)]

for i in permutations(l, m):
    print(*i)