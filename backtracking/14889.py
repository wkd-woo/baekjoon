import copy
from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

p = [i for i in range(n)]
ans = int(1e9)

for one in combinations(p, n // 2):
    s = []
    l = []
    two = copy.deepcopy(p)
    for i in one:
        two.remove(i)
    for a, b in combinations(one, 2):
        s.append(graph[a][b])
        s.append(graph[b][a])

    for a, b in combinations(two, 2):
        l.append(graph[a][b])
        l.append(graph[b][a])

    ans = min(ans, abs(sum(s) - sum(l)))

print(ans)
