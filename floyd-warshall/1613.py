from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

# 플로이드-워셜 알고리즘
for k in range(n):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] or (graph[i][k] and graph[k][j]):
                graph[i][j] = 1  # 먼저 일어난 경우

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if not graph[a - 1][b - 1]:
        if graph[b - 1][a - 1]:
            print(1)
        else:
            print(0)
    else:
        print(-1)