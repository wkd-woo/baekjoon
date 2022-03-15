INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n = int(input())
target = list(map(int, input().split()))
m = int(input())

graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1

# 플로이드-워셜 알고리즘
for k in range(n):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    # 자기 자신과 관계는 0
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[target[0] - 1][target[1] - 1] != INF:
    print(graph[target[0] - 1][target[1] - 1])
else:
    print(-1)