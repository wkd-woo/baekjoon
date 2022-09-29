import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


n, m = map(int, input().split())
tree = {i: [] for i in range(1, n + 1)}
visited = {i: 0 for i in range(1, n + 1)}
plus = {i: 0 for i in range(1, n + 1)}

l = list(map(int, input().split()))

for i, w in enumerate(l):
    if i == 0:
        continue
    tree[w].append(i + 1)


def dfs(cur):  # 내리칭찬
    visited[cur] = True
    for next_ in tree[cur]:
        if not visited[next_]:
            plus[next_] += plus[cur]
            dfs(next_)
    return


for _ in range(m):
    u, p = map(int, input().split())
    plus[u] += p

dfs(1)
answer = list(plus.values())
print(*answer)