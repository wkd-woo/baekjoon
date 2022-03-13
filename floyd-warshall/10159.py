from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())

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
                graph[i][j] = 1  # 가벼운 경우

# 출력
for i in range(n):
    know = 0
    for j in range(n):
        know += graph[i][j] + graph[j][i]  # 가벼운 물건과 무거운 물건의 합

    print(n - 1 - know)
