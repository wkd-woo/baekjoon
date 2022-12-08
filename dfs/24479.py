import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(node):
    global cnt
    visited[node] = cnt  # check
    cnt += 1
    for next_ in sorted(graph[node]):
        if visited[next_] == 0:
            dfs(next_)

    return


n, m, r = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
visited = {i: 0 for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

global cnt
cnt = 1
dfs(r)

for i in range(1, n+1):
    print(visited[i])
