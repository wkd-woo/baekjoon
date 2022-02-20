from collections import deque


def dfs(graph, start_node):
    visited = []
    stack = deque()

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack += reversed(graph[node])

    for each in visited:
        print(each, end=' ')


def bfs(graph, start_node):
    queue, visited = deque(), list()
    queue.append(start_node)

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    for each in visited:
        print(each, end=' ')


# 정점, 간선, 시작점 입력
points, lines, start = map(int, input().split())

if 1 <= points <= 1000 and 1 <= lines <= 10000:

    # 이차원 배열의 행을 정점 개수만큼
    graph = {i: [] for i in range(1, points + 1)}
    graph
    for _ in range(1, lines + 1):
        node_1, node_2 = map(int, input().split())
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    for key in graph:
        graph[key].sort()

    dfs(graph, start)
    print()
    bfs(graph, start)

# 이차원 배열의 행을 정점 개수만큼
# temp = [[] for _ in range(points)]

# dict 형태로 연결된 정점을 입력
# graph = {i + 1: temp[i] for i in range(len(temp))}
