from sys import stdin

input = stdin.readline

n = int(input())

graph = {i: [] for i in range(1, n+1)}
edges = {}
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    edges[i+1] = (a, b)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())

    if t == 1:  # 단절점
        if len(graph[k]) == 1:  # 리프 노드인 경우 단절점 X
            print('no')
        else:
            print('yes')

    elif t == 2:
        print('yes')
