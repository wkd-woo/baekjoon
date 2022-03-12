from sys import stdin

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

input = stdin.readline

n, m = map(int, input().split())
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1

# 플로이드-워셜 알고리즘
for k in range(n):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    # 자기 자신과 관계는 0
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == INF:
            graph[i][j] = 0

# 출력
result = (0, INF)
for row in range(n):
    if 0 < sum(graph[row]) < result[1]:
        result = (row, sum(graph[row]))

print(result[0] + 1)
