from sys import stdin
from itertools import combinations


input = stdin.readline


def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p
    return p


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
db = {i+1: type_ for i, type_ in enumerate(list(input().split()))}
parent, edges = [i for i in range(n+1)], []
for _ in range(m):
    u, v, cost = map(int, input().split())
    if db[u] != db[v]:
        edges.append((cost, min(u, v), max(u, v)))


result = 0
edges.sort()
for edge in edges:
    cost, u, v = edge
    if find(u) != find(v):
        union(u, v)
        result += cost

for i in range(1, n+1):
    find(i)


print(result) if len(set(parent[1:])) == 1 else print(-1)
