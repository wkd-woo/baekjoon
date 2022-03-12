from sys import stdin

input = stdin.readline

n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(input())

visited = [[0] * n for _ in range(n)]

# 플로이드-워셜 알고리즘
for k in range(n):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                visited[i][j] = 1

result = 0
for row in visited:
    result = max(result, sum(row))

print(result)