import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline



def dfs(graph, start, visited):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

    return visited


t = int(input())

for _ in range(t):
    n = int(input())
    tree = {i: [] for i in range(1, n + 1)}

    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[v].append(u)

    one, two = map(int, input().split())
    visited = {i: 0 for i in range(1, n + 1)}
    result = dfs(tree, one, [])
    visited = {i: 0 for i in range(1, n + 1)}
    result2 = set(dfs(tree, two, []))
    for r1 in result:
        if r1 in result2:
            print(r1)
            break