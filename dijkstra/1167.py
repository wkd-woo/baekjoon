from collections import defaultdict, deque

V = int(input())
tree = defaultdict(list)
for _ in range(V):
    l = deque(map(int, input().split()))
    l.pop()
    u = l.popleft()
    while l:
        v = l.popleft()
        w = l.popleft()
        tree[u].append([v, w])


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


diameter_max, mx_node = -int(1e9), 0
visited = [False] * (V + 1)

visited[1] = True
dfs(1, 0, visited)
visited[1] = False
visited[mx_node] = True
dfs(mx_node, 0, visited)
visited[mx_node] = False

print(diameter_max)
