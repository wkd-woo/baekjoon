k = int(input())
w = list(map(int, input().split()))
V, E = 2**(k+1) - 1, 2**(k+1) - 2

tree = {i: [] for i in range(1, V+1)}
parent = {i: [i//2] for i in range(1, V+1)}
parent[1] = [1]


def dfs(graph, start, visited=[]):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

    return visited
