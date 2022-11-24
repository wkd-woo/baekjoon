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


n = int(input())
parent, edges = [i for i in range(n+1)], []
planet = []
for i in range(n):
    x, y, z = map(int, input().split())
    planet.append((i, x, y, z))

planetX = sorted(planet, key=lambda x: x[1])
planetY = sorted(planet, key=lambda x: x[2])
planetZ = sorted(planet, key=lambda x: x[3])
for A, B in zip(planetX, planetX[1:]):
    u, xA, yA, zA = A
    v, xB, yB, zB = B
    cost = min(abs(xA - xB), abs(yA - yB), abs(zA - zB))
    edges.append((cost, u, v))

for A, B in zip(planetY, planetY[1:]):
    u, xA, yA, zA = A
    v, xB, yB, zB = B
    cost = min(abs(xA - xB), abs(yA - yB), abs(zA - zB))
    edges.append((cost, u, v))

for A, B in zip(planetZ, planetZ[1:]):
    u, xA, yA, zA = A
    v, xB, yB, zB = B
    cost = min(abs(xA - xB), abs(yA - yB), abs(zA - zB))
    edges.append((cost, u, v))

answer = 0
edges.sort()
for edge in edges:
    cost, u, v = edge
    if find(u) != find(v):
        union(u, v)
        answer += cost

print(answer)
