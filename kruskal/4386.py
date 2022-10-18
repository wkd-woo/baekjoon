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


n = int(input())

parent, edges = [i for i in range(100 + 1)], []
planet = []
for i in range(n):
    x, y = map(float, input().split())
    planet.append((i, x, y))

for one, two in list(combinations(planet, 2)):
    u, x_one, y_one = one
    v, x_two, y_two = two
    cost = round(((x_one - x_two)**2 + (y_one - y_two) ** 2) ** 0.5, 2)
    edges.append((cost, u, v))


edges.sort()
answer = 0
for edge in edges:
    cost, u, v = edge
    if find(u) != find(v):
        union(u, v)
        answer += cost

print(answer)
