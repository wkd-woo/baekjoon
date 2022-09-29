import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


N = int(input())
tree = {i: [] for i in range(1, N + 1)}
parent = {i: [i] for i in range(1, N + 1)}
for i in range(N):
    node, left, right = map(int, (input().split()))
    tree[node] = [left, right]
    if left != -1:
        parent[left] = [node]
    if right != -1:
        parent[right] = [node]


def dfs(graph, start, visited=[]):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

    return visited


def inorder(start):
    if start != -1:
        if tree[start][0] != - 1:
            inorder(tree[start][0])
        global result
        result.append(start)
        if tree[start][1] != - 1:
            inorder(tree[start][1])


result = list()
inorder(1)
last = result[-1]
dfs(parent, last)
answer = len(result) * 2 - len(dfs(parent, last))
print(answer)