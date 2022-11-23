from sys import stdin

input = stdin.readline





n, m = map(int, input().split())
parent, edges = [i for i in range(n+1)], []

costs = 0
for _ in range(m):
    u, v, cost = map(int, input().split())
    edges.append((cost, u, v))
    costs += cost

answer = 0
edges.sort()
for cost, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        answer += cost


for x in range(1, n+1):
    find(x)

if len(set(parent)) != 2:
    print(-1)
else:
    print(costs - answer)
