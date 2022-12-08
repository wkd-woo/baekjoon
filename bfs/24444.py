import sys
from collections import deque

input = sys.stdin.readline


def bfs(node):
    cnt = 1
    q = deque([node])
    while q:
        now = q.popleft()
        if visited[now] == 0:
            visited[now] = cnt
            cnt += 1
            for next_ in sorted(graph[now]):
                if visited[next_] == 0:
                    q.append(next_)

    return


n, m, r = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
visited = {i: 0 for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(r)

for i in range(1, n+1):
    print(visited[i])
