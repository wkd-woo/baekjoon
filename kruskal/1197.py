from sys import stdin

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

parent, edges = [i for i in range(10000 + 1)], []
for _ in range(m):
    u, v, cost = map(int, input().split())
    edges.append((cost, u, v))

edges.sort()
answer = 0
for edge in edges:
    cost, u, v = edge
    if find(u) != find(v):
        union(u, v)
        answer += cost

print(answer)
