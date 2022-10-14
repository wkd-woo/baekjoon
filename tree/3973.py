from collections import defaultdict, deque


def dfs(node, dist, visited):
    global diameter_max, mx_node
    if diameter_max < dist:
        diameter_max = max(diameter_max, dist)
        mx_node = node

    for nxt_node, nxt_dist in tree[node]:
        if not visited[nxt_node]:
            visited[nxt_node] = True
            dfs(nxt_node, dist + nxt_dist, visited)
            visited[nxt_node] = False


for _ in range(int(input())):
    n = int(input())
    tree = {i: [] for i in range(n)}

    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a].append([b, 1])
        tree[b].append([a, 1])

    visited = [False] * (n + 1)
    diameter_max, mx_node = -int(1e9), 0

    visited[1] = True
    dfs(1, 0, visited)
    visited[1] = False
    visited[mx_node] = True
    dfs(mx_node, 0, visited)
    visited[mx_node] = False

    print(diameter_max)
