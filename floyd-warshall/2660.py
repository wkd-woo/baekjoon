import sys

input = sys.stdin.readline

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
n = int(input())
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for k in range(n):
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer, candidates = [], []
for i in range(n):
    answer.append(max(graph[i]))

MIN = min(answer)
print(MIN, answer.count(MIN))

for i in range(0, n):
    if answer[i] == MIN:
        candidates.append(i + 1)

print(*candidates)
