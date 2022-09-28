n, r, q = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
tree = {i: [] for i in range(1, n + 1)}
parents = {i: i for i in range(1, n + 1)}

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


# 그래프로 트리만들기
def makeTree(cur, parent):
    for node in graph[cur]:
        if node != parent:
            tree[cur].append(node)
            parents[node] = cur
            makeTree(node, cur)


def dfs(root):
    visited = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(tree[node])
    return visited


makeTree(5, -1)

for _ in range(q):
    u = int(input())
    print(len(dfs(u)))

#######################

import sys

sys.setrecursionlimit(150000)
input = sys.stdin.readline
n, r, q = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
visited = {i: 0 for i in range(1, n + 1)}

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(cur, visited):
    visited[cur] += 1
    for next in graph[cur]:
        if not visited[next]:
            visited[cur] += dfs(next, visited)
    return visited[cur]


dfs(r)

for _ in range(q):
    u = int(input())
    print(visited[u])
