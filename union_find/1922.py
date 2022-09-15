n = int(input())
m = int(input())


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


parent, edges = [i for i in range(0, 1000 + 1)], []
for _ in range(m):
    u, v, cost = map(int, input().split())
    edges.append((cost, u, v))

edges.sort()

answer = 0
for i in range(m):
    cost, u, v = edges[i]
    if find(u) != find(v):
        union(u, v)
        answer += cost

print(answer)
