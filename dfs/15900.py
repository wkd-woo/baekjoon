n = int(input())
tree = {i: [] for i in range(1, n + 1)}
visited = [False for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)


def dfs(cur):
    visited[cur] = True
    for next in tree[cur]:
        if not visited[next]:
            distance[next] = distance[cur] + 1
            dfs(next)


dfs(1)
answer = 0
for K, V in tree.items():
    if len(V) == 1:
        answer += distance[K]

if answer % 2:
    print('Yes')
else:
    print('No')