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
edges = [list(map(int, input().split()))]
for _ in range(m):
    edges.append(list(map(int, input().split())))
edges = [[not edge[2], min(edge[0], edge[1]), max(edge[0], edge[1])]
         for edge in edges]


# 최선 - 최악의 경우의 수 -> 최대/최소 스패닝 트리 0일때 또는 1일때
mn = 0
parent = [i for i in range(1000001)]
edges.sort()
for edge in edges:
    cost, u, v = edge
    if find(u) != find(v):
        union(u, v)
        mn += cost

mx = 0
parent = [i for i in range(1000001)]
edges.sort(reverse=True)
for edge in edges:
    cost, u, v = edge
    if find(u) != find(v):
        union(u, v)
        mx += cost


# 최악 - 최선
print(abs(mx**2 - mn**2))
