from collections import deque


def bfs(graph, start_node):
    visited = list()
    queue = deque()  # need_visit

    queue.append(start_node)

    while queue:
        node = queue.popleft()  # deque로 선언하여 popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited

def dfs(graph, start_node):
    visited, stack = list(), list()

    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

    return visited

n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

print(*dfs(graph, v))
print(*bfs(graph, v))