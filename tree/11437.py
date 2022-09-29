import sys

sys.setrecursionlimit(int(1e5))

n = int(input())

parent = [0] * (n + 1)
d = [0] * (n + 1)
c = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, depth): # 노드의 깊이 추적
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:
            continue
        parent[y] = x
        dfs(y, depth + 1)


def lca(a, b): # 공통 조상 추적
    while d[a] != d[b]: # 깊이가 같아질 때 까지 올라감
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b: # 부모가 같아질 때 까지 또 올라감
        a = parent[a]
        b = parent[b]
    return a


dfs(1, 0)

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))