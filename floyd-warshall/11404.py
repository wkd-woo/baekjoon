from sys import stdin

input = stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n = int(input())
m = int(input())
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start - 1][end - 1] = min(graph[start - 1][end - 1], cost)

# 플로이드-워셜 알고리즘
for k in range(n):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    # 자기 자신과 관계는 0
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력
for row in graph:
    for col in row:
        print(col, end=" ")
    print()
