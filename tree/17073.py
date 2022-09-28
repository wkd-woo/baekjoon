import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, w = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
tree = {i: [] for i in range(1, n + 1)}
parents = {i: i for i in range(1, n + 1)}
possibility = {i: 1 for i in range(1, n + 1)}
visited = {i: 0 for i in range(1, n + 1)}

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


def dfs(cur):
    visited[cur] = True
    for next in graph[cur]:
        if not visited[next]:
            possibility[next] = possibility[cur] * len(tree[cur])
            dfs(next)
    return


makeTree(1, -1)
dfs(1)
exp, leaves = 0, 0
for K, V in tree.items():
    if not V:
        leaves += 1
        pos = 1 / possibility[K]
        exp += (w * pos)

print(exp / leaves)
