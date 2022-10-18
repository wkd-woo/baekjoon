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


n = int(input())

parent, edges = [i for i in range(1000 + 1)], []
for i in range(n):
    costs = list(map(int, input().split()))
    for j in range(len(costs)):
        if i == j:
            continue
        edges.append((costs[j], i, j))

edges.sort()
answer = 0
for edge in edges:
    cost, u, v = edge
    if find(u) != find(v):
        union(u, v)
        answer += cost

print(answer)
