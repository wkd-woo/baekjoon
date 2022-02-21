import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())


# 인접기반 그래프 순회, 방문 안된 노드 방문 -> 현재 node와 같은 연결요소
def dfs(node):
    visited[node] = True
    for each in graph[node]:
        if not visited[each]:
            dfs(each)


# 인접기반 연결리스트 구현 > 연결리스트는 graph[정점] == 배열
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

if 1 <= n < 10000 and 0 <= m <= (n * (n - 1) / 2):
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        if not visited[i]:
            count += 1
            dfs(i)

    print(count)
