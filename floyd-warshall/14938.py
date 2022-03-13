from sys import stdin

input = stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[INF] * n for _ in range(n)]

for _ in range(r):
    start, end, cost = map(int, input().split())
    graph[start - 1][end - 1] = min(graph[start - 1][end - 1], cost)
    graph[end - 1][start - 1] = min(graph[end - 1][start - 1], cost)

# 플로이드-워셜 알고리즘
for k in range(n):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

maxItem = 0
for each in graph:
    tmp = 0
    for i in range(n):
        if each[i] <= m:
            tmp += items[i]
    maxItem = max(maxItem, tmp)

print(maxItem)
