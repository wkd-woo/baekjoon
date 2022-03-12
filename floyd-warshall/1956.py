from sys import stdin

input = stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

v, e = map(int, input().split())
graph = [[INF] * v for _ in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)

# 플로이드-워셜 알고리즘
for k in range(v):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(v):
        for j in range(v):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력
course = INF
for i in range(v):
    course = min(graph[i][i], course)

if course != INF:
    print(course)
else:
    print(-1)