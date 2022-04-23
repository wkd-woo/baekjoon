INF = int(1e9)

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

crashed = [[0] * m for _ in range(n)]

res = int(INF)


def bfs():
    visited = [[INF] * m for _ in range(n)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]  # 상하좌우 돌면서 확인
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                if visited[nx][ny] == INF:
                    visited[nx][ny] = visited[x][y] + 1  # 방문기록
                    queue.append((nx, ny))  # 현 위치 좌표를 queue에 추가
                elif visited[nx][ny] != INF and visited[x][y] + 1 < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))  # 현 위치 좌표를 queue에 추가

    global res
    if visited[n - 1][m - 1] != -1:
        res = min(res, visited[n - 1][m - 1])


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not crashed[i][j]:
            graph[i][j] = 0
            crashed[i][j] = 1
            bfs()
            graph[i][j] = 1

print(res if res != int(1e9) else -1)