from sys import stdin
from itertools import combinations


input = stdin.readline


def find(x):
    if x == parent[x]:
        return x
    else:
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
coords = [(i+1, tuple(map(int, input().split()))) for i in range(n)]
linked = [list(map(int, input().split())) for _ in range(m)]

# 작은것 - 큰것 순으로 순서 일치시켜야함
linked = [[min(each), max(each)] for each in linked]
parent, edges = [i for i in range(1001)], []
for one, two in combinations(coords, 2):
    u, uxy = one
    v, vxy = two
    ux, uy = uxy
    vx, vy = vxy

    cost = ((ux - vx)**2 + (uy - vy) ** 2) ** 0.5
    edges.append((cost, min(u, v), max(u, v)))


answer = 0
for edge in linked:
    u, v = edge
    if find(u) != find(v):
        union(u, v)

edges.sort()
for edge in edges:
    cost, u, v = edge
    if find(u) != find(v):
        union(u, v)
        answer += cost


print("{:.2f}".format(answer))
