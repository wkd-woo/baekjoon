from sys import stdin

input = stdin.readline
n, m = map(int, input().split())

graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

# 플로이드-워셜 알고리즘
for k in range(n):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] or (graph[i][k] and graph[k][j]):
                graph[i][j] = 1  # 자신보다 작은 경우

# 출력
result = 0
for i in range(n):
    know = 0
    for j in range(n):
        know += graph[i][j] + graph[j][i]  # 자신보다 작은사람과 큰사람의 합
    if know == n - 1:  # 자신의 키 순서를 알 경우
        result += 1

print(result)