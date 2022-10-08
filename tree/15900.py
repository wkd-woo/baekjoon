k = int(input())
w = list(map(int, input().split()))
V, E = 2**(k+1) - 1, 2**(k+1) - 2

tree = {i: [] for i in range(1, V+1)}
parent = {i: [i//2] for i in range(1, V+1)}
parent[1] = [1]


for v in range(V, 1, -1):
    tree[v//2].append((v, w[v-2]))

leaves = [K for K, V in tree.items() if not V]
visited = [False for _ in range(V + 1)]
distance = [0 for _ in range(V + 1)]


def dfs(cur):
    visited[cur] = True
    for next_, weight in tree[cur]:
        if not visited[next_]:
            distance[next_] = distance[cur] + weight
            dfs(next_)


dfs(1)
print(sum(distance))
