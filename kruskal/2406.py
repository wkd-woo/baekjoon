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
link = [list(map(int, input().split())) for _ in range(m)]
parent, edges = [i for i in range(n+1)], []
networks = []
for i in range(1, n+1):
    l = list(map(int, input().split()))
    networks.append(l)
    for j in range(len(l)):
        if i == j + 1:
            continue
        if i == 1 or j + 1 == 1:
            continue
        edges.append((l[j], i, j + 1))

for u, v in link:
    if find(u) != find(v) and u != 1:
        union(u, v)

costs, k, computers = 0, 0, []
edges.sort()
for edge in edges:
    cost, u, v = edge
    if find(u) != find(v):
        union(u, v)
        costs += cost
        k += 1
        computers.append((u, v))

print(costs, k)
for link in computers:
    print(*link)
