import sys

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

distance = [[INF for _ in range(n)] for _ in range(n)]
pre_node = [[0 for _ in range(n)] for _ in range(n)] # 이전 node 기억하는 그래프

for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a - 1][b - 1] = min(distance[a - 1][b - 1], c)
    distance[b - 1][a - 1] = min(distance[b - 1][a - 1], c)

    pre_node[a - 1][b - 1] = b
    pre_node[b - 1][a - 1] = a

for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                pre_node[i][j] = pre_node[i][k] # 이전 노드 변경

for i in range(n):
    pre_node[i][i] = '-'
for row in pre_node:
    print(*row)
