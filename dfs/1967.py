def dfs(node, w):
    for i in tree[node]:
        a, b = i
        if distance[a] == -1:
            distance[a] = w + b
            dfs(a, w + b)


n = int(input())
tree = [[] for _ in range(n + 1)]

for i in range(n - 1):
    s, e, d = map(int, input().split())
    tree[s].append((e, d))
    tree[e].append((s, d))

distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)
print(max(distance))